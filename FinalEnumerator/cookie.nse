
-- HEAD --
local shortport = require "shortport"
local http = require "http"
local stdnse = require "stdnse"

description = [[ Get Cookies!! - Test script for ops challenge 35 - 
author = Ben Podawiltz 
resource: https://youtube.com/watch?v=y2z8zUanmL4 #NMAP Scripts with LUA and NSE Paul's Security Weekly 
]]
categories = {"safe"}
-- RULE --

portrule = shortport.http


-- ACTION --

action = function(host, port)
  local path = nmap.registry.args.path

  if(path == nil) then
    path = '/'
  end	

  local response = http.get(host, port, path)
  local cookiejar = {}

  for _, cookie in pairs(response.cookies) do
    table.insert(cookiejar, "Cookie: name" .. cookie.name .. "; value=" .. cookie.value)
  end

  return stdnse.format_output(true, cookiejar)

end



