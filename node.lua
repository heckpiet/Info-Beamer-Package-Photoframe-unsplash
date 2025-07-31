--[[
Unsplash Photoframe for Info-Beamer
----------------------------------

Displays downloaded Unsplash images as a slideshow. The list of images is read
from the ``images/`` directory. If no images are found, a placeholder screen is
shown.

Copyright (C) 2025
Released under the GPLv3 license.
]]

local json = require "json"
local CONFIG = json.decode(resource.load_file("config.json"))
FONT = resource.load_font("Roboto-Regular.ttf")

local function parse_color(hex)
    local r = tonumber(hex:sub(2,3), 16) / 255
    local g = tonumber(hex:sub(4,5), 16) / 255
    local b = tonumber(hex:sub(6,7), 16) / 255
    local a = tonumber(hex:sub(8,9), 16) / 255
    return r, g, b, a
end

local rotation = CONFIG.rotation.value or 0
local show_clock = CONFIG.show_clock.value
local clock_x = CONFIG.clock_pos_x.value or 10
local clock_y = CONFIG.clock_pos_y.value or 10
local clock_r, clock_g, clock_b, clock_a = parse_color(CONFIG.clock_color.value or "#ffffffff")
local image_list = {}
local idx = 1
local last_switch = sys.now()
local offline = false

local function check_offline()
    local status, data = pcall(resource.load_file, "offline.flag")
    offline = status and data ~= nil
end

function reload_images()
    image_list = {}
    local p = io.popen("ls images/*.jpg 2>/dev/null")
    for file in p:lines() do
        table.insert(image_list, resource.load_image(file))
    end
    p:close()
end

node.event("file_change", function(filename)
    if filename:match("images/.*%.jpg") then
        reload_images()
    end
    if filename == "offline.flag" then
        check_offline()
    end
end)

function node.render()
    if #image_list == 0 then
        gl.clear(0, 0, 0, 1)
        local msg = "No cached images" -- offline/empty hint
        local w = math.floor(NATIVE_WIDTH / 2 - FONT:width(msg, 50) / 2)
        FONT:write(w, NATIVE_HEIGHT / 2 - 25, msg, 50, 1,1,1,1)
        return
    end
    if sys.now() - last_switch > (CONFIG.slideshow_delay.value or 10) then
        idx = idx % #image_list + 1
        last_switch = sys.now()
    end
    gl.clear(0, 0, 0, 1)

    gl.pushMatrix()
    gl.translate(NATIVE_WIDTH/2, NATIVE_HEIGHT/2)
    gl.rotate(rotation)
    gl.translate(-NATIVE_WIDTH/2, -NATIVE_HEIGHT/2)

    local img = image_list[idx]
    if img then
        img:draw(0, 0, NATIVE_WIDTH, NATIVE_HEIGHT, 1)
    end
    gl.popMatrix()

    if show_clock then
        local now = os.date("%Y-%m-%d %H:%M:%S")
        FONT:write(clock_x, clock_y, now, 30, clock_r, clock_g, clock_b, clock_a)
    end
    if offline then
        local msg = "OFFLINE MODE"
        local w = math.floor(NATIVE_WIDTH / 2 - FONT:width(msg, 30) / 2)
        FONT:write(w, 30, msg, 30, 1, 0, 0, 1)
    end
end

reload_images()
check_offline()
