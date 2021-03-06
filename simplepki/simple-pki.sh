#!/bin/bash

echo "This is a simple pki script."

echo "Creating root directories...
mkdir -p ca/root-ca/private ca/root-ca/db crl certs
chmod 700 ca/root-ca/private

echo "creating database...."
cp /dev/null ca/root-ca/db/root-ca.db
cp /dev/null ca/root-ca/db/root-ca.db.attr
echo 01 > ca/root-ca/db/root-ca.crt.srl
echo 01 > ca/root-ca/db/root-ca.crl.srl


echo "creating Certicate Authority request..."
openssl req -new \
    -config etc/root-ca.conf \
    -out ca/root-ca.csr \
    -keyout ca/root-ca/private/root-ca.key


echo "creating Certificate Authority certificate..."
openssl ca -selfsign \
    -config etc/root-ca.conf \
    -in ca/root-ca.csr \
    -out ca/root-ca.crt \
    -extensions root_ca_ext

echo "Creating directories..."
mkdir -p ca/signing-ca/private ca/signing-ca/db crl certs
chmod 700 ca/signing-ca/private

echo "creating database..."
cp /dev/null ca/signing-ca/db/signing-ca.db
cp /dev/null ca/signing-ca/db/signing-ca.db.attr
echo 01 > ca/signing-ca/db/signing-ca.crt.srl
echo 01 > ca/signing-ca/db/signing-ca.crl.srl

echo "Creating CA request..."
openssl req -new \
    -config etc/signing-ca.conf \
    -out ca/signing-ca.csr \
    -keyout ca/signing-ca/private/signing-ca.key

echo "creating CA certificate..."
openssl ca \
    -config etc/root-ca.conf \
    -in ca/signing-ca.csr \
    -out ca/signing-ca.crt \
    -extensions signing_ca_ext

echo "create email request...for this section use the following sample information so all the certificates are identical..."
echo "When prompted enter these DN components: DC=org, DC=simple, O=Simple Inc, CN=Fred Flintstone, emailAddress=fred@simple.org. Leave other fields empty."
openssl req -new \
    -config etc/email.conf \
    -out certs/fred.csr \
    -keyout certs/fred.key


echo "creating email certificate..."
openssl ca \
    -config etc/signing-ca.conf \
    -in certs/fred.csr \
    -out certs/fred.crt \
    -extensions email_ext

echo "creating TLS server request..."
echo "When prompted enter these DN components: DC=org, DC=simple, O=Simple Inc, CN=www.simple.org. Note that the subjectAltName must be specified as environment variable"
SAN=DNS:www.simple.org \
openssl req -new \
    -config etc/server.conf \
    -out certs/simple.org.csr \
    -keyout certs/simple.org.key

echo "creating TLS server certificate..."
openssl ca \
    -config etc/signing-ca.conf \
    -in certs/simple.org.csr \
    -out certs/simple.org.crt \
    -extensions server_ext

echo "creating Revoke certificate..."
openssl ca \
    -config etc/signing-ca.conf \
    -revoke ca/signing-ca/01.pem \
    -crl_reason superseded

echo "creating CRL..."
openssl ca -gencrl \
    -config etc/signing-ca.conf \
    -out crl/signing-ca.crl

echo "creating DER certificate..."
openssl x509 \
    -in certs/fred.crt \
    -out certs/fred.cer \
    -outform der

echo "creating PKCS#7 bundle...."
openssl crl2pkcs7 -nocrl \
    -certfile ca/signing-ca.crt \
    -certfile ca/root-ca.crt \
    -out ca/signing-ca-chain.p7c \
    -outform der

echo "creating PKCS #12 bundle..."
openssl pkcs12 -export \
    -name "Fred Flintstone" \
    -inkey certs/fred.key \
    -in certs/fred.crt \
    -out certs/fred.p12

echo "creating PEM bundle..."
cat ca/signing-ca.crt ca/root-ca.crt > \
    ca/signing-ca-chain.pem

cat certs/fred.key certs/fred.crt > \
    certs/fred.pem

echo "View results...."
openssl req \
    -in certs/fred.csr \
    -noout \
    -text

echo "View certificates..."
openssl x509 \
    -in certs/fred.crt \
    -noout \
    -text "

echo "View CRL...."
openssl crl \
    -in crl/signing-ca.crl \
    -inform der \
    -noout \
    -text

echo "View PKCS#7 bundle..."
openssl pkcs7 \
    -in ca/signing-ca-chain.p7c \
    -inform der \
    -noout \
    -text \
    -print_certs

echo "view PKCS#12 bundle...."
openssl pkcs12 \
    -in certs/fred.p12 \
    -nodes \
    -info

echo "End of script"


###################
#
# Source: https://pki-tutorial.readthedocs.io/en/latest/simple/
#
# End