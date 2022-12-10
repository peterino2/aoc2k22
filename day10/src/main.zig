const std = @import("std");
const input = @embedFile("day10.input");

pub fn main() !void {
    var iter = std.mem.tokenize(u8, input, "\n");
    var cycleCount: i32 = 0;
    var currentCycleCount: i32 = 0;
    var regx: i32 = 1;
    var executing: bool = true;
    var line:[]const u8 = "noop";
    var shouldProceed: bool = true;
    var offsets: [7] i32 = std.mem.zeroes([7] i32);
    var nextCycle: usize = 20;
    var offsetCount: usize = 0;
    var currentPixelDraw: i32 = 0;

    while(executing)
    {
        cycleCount += 1;
        if(shouldProceed)
        {
            line = iter.next() orelse break;
        }

        if(cycleCount == nextCycle )
        {
            if(cycleCount <= 220)
            {
                offsets[offsetCount] = regx * cycleCount;
                nextCycle += 40;
                offsetCount += 1;
            }
        }

        currentPixelDraw = @mod(cycleCount - 1, 40);
        var delta: i32 = try std.math.absInt( currentPixelDraw - (regx));
        var visible: bool = delta < 2;

        // std.debug.print("during: regx = {d} cycleCount = {d} {d} strength={d}\n", .{regx, cycleCount, currentCycleCount, cycleCount * regx});
        //std.debug.print("currentPixelDraw={d} regx={d} visible={any}\n", .{currentPixelDraw , regx, visible});
        std.debug.print("{s}", .{if (visible) "#" else ".",});

        if(@mod(cycleCount, 40) == 0)
        {
            std.debug.print("\n", .{});
        }

        if(std.mem.eql(u8, "noop", line[0..4]))
        {
            currentCycleCount = 0;
            shouldProceed = true;
        }
        if(std.mem.eql(u8, "addx", line[0..4]))
        {
            currentCycleCount += 1;
            shouldProceed = false;
            var addx = try std.fmt.parseInt(i32, line[5 .. line.len], 10);
            if(currentCycleCount == 2)
            {
                regx += addx;
                currentCycleCount = 0;
                shouldProceed = true;
            }
        }
    }
    var sum: i32 = 0;
    for (offsets) |offset|
    {
        sum += offset;
    }
    std.debug.print("sum = {d}\n", .{sum});
}