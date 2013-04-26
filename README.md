lodDescriptions
===============

A hierarchical scene-graph arranged approach to text descriptions, allowing objects/characters to be described to different extents depending on the level of detail requested.

##Objective 

To generate novel creatures and objects using a component-based approach that combines random elements to form a hierarchical scene-graph description, which can then be processed during a traversal to yield a text description of the thing. 

Using this scene-graph, different levels of detail are then to be used in prompting descriptive textual outputs of differing length and detail, by using some indication of importance of information and some means of collapsing explicit sub-component descriptions to produce vaguer textual descriptions.

## Current side investigations

### Auto-indenting hierarchical printing

Use of wrappers to facilitate automatic white-spacing for improving print outputs of hierarchical information. 

Currently, function calls contibute to a global whitespace variable which tracks how much whitespace should be inserted ahead of the next print-output. The function utils.iPrint() enforces the indented printing based on the whitespace variable, and utils.wsWrapper() uses utils.incWhitespace() and utils.decWhitespace() before and after the wrapped function to enforce the incrementing/decrementing of the whitespace global variable.
