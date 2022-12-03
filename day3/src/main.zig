const std = @import("std");
const file: []const u8 = @embedFile("day3.input");

// define a rucksack as an array of 52 unsigned 8s this allows us to do a masking operation with them
const RuckSack = [52] u8;

pub fn main() !void {
    // split the file according to newlines
    var tokens = std.mem.tokenize(u8, file, "\n");
    // === part 2 stuff ===
    var group_count: usize = 0;
    // this array shall be ANDed with two subsequent rucksacks to determine which item represents the badge
    var group_badge: [52] u8 = std.mem.zeroes([52] u8); 
    // === part 2 stuff ===

    var group_priority_total: usize = 0; // needed for part 2
    var total_priority: usize = 0;

    // for each line...
    while(tokens.next()) |token|
    {
        // allocate two rucksack compartments
        var rucksack_compartments: [2]RuckSack = std.mem.zeroes([2]RuckSack);
        var rucksack_total: RuckSack = std.mem.zeroes(RuckSack); // garuntee zero-init of rucksacks

        var i: usize = 0;
        while(i < token.len) : (i += 1)
        {
            // if we're in the left side of the string, use rucksack compartment 0, otherwise use rucksack compartment 1
            var ruck: usize = if (i < token.len / 2) 0 else 1;

            // map char ranges from 'a' - 'z' from 0 to 25
            // and map char ranges from 'A' - 'Z' from 26 - 51
            // these chars can directly be stored into a RuckSack with an index operation
            var l: u8 = if (token[i] >= 'a') 
                    token[i] - 'a'
                else 
                    token[i] - 'A' + 26;
            rucksack_compartments[ruck][@intCast(usize, l)] = 1;

            // part 2; if this is the first set in a new group record it into the group_badge rucksack for subsequent
            // masking operations
            if(group_count == 0)
            {
                group_badge[l] = 1;
            }

            rucksack_total[l] = 1;
        }

        // mask the group rucksack against the current rucksack
        for(rucksack_total) |ruckItem, index|
        {
            group_badge[index] = group_badge[index] & ruckItem;
        }

        // mask rucksack compartment 0 against rucksack compartment 1
        var priority: usize = 0;
        for(rucksack_compartments[0]) |ruck0Item, itemIndex|
        {
            if(letters[1][itemIndex] & ruck0Item > 0)
            {
                // any union of the two must be an item with priority that we can add to the total score
                priority += itemIndex + 1; 
            }
        }
        total_priority += priority;

        // === part 2 code ===
        group_count += 1;
        // reached end of trio group
        // check which items have not been masked out, that must then be the badge.
        if(group_count == 3)
        {
            for(group_badge) |badge, badgeIndex|
            {
                if(badge > 0)
                {
                    group_priority_total += badgeIndex + 1;
                }
            }
            group_badge = std.mem.zeroes([52] u8);
            group_count = 0;
        }
        // === end of part 2 code ===
    }

    // print results
    std.debug.print("total priority: {d} total_group_priority: {d}", .{total_priority, group_priority_total});
}