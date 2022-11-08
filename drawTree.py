# define a tree function
def tree(h, levels):
    """This function is recursive: it calls itself."""
    line((0, 0), (0, h))  # draw a branch
    if levels <= 1:
        return  # we've drawn all levels, stop
    # branch into two random angles
    for angle in [random() * 30, random() * -30]:
        # use "with savedState()" to keep the transformations local
        with savedState():
            # move the origin to the tip of the branch
            translate(0, h)
            rotate(angle)  # wibble wobble
            scale(0.65 + 0.25 * random())  # next branch will be smaller
            tree(h, levels - 1) # draw another tree at the tip of the branch

# set the canvas size
size(600, 600)
# move the origin to the bottom middle of the canvas,
# this is where the base of the tree will be
translate(width() / 2, 30)

# set some paint properties
fill(None)
stroke(255, 0, 0)
strokeWidth(10)
lineCap("round")

# draw a tree!
tree(100, 11)  # be careful with higher level values, it may take forever to complete!
