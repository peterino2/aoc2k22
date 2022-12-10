const std = @import("std");
const helpers = @import("helpers");
const input = @embedFile("day6.input");

pub fn main() !void {
    find_start_of_stream(input, 4);
    find_start_of_stream(input, 14);
}

pub fn find_start_of_stream(text: []const u8, tokenSize: usize) void
{
    var i: usize = tokenSize;
    while (i < text.len) : (i += 1)
    {
        const slice = text[i - tokenSize..i];
        if(helpers.allCharsUnique(slice))
        {
            std.debug.print("found: {d}\n", .{i});
            return;
        }
    }
}


pub fn allCharsUnique(str:[] const u8) bool
{
    var counts:[26] u8 = std.mem.zeroes([26]u8);
    var dupe_found: bool = false;
    for(str) |c|
    {
        if(counts[c - 'a'] > 0)
        {
            dupe_found = true;
            break;
        }
        counts[c - 'a'] += 1;
    }
    return !dupe_found;
}