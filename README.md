# Overview

This is a Python 3 implementation of a (3x3) Rubik's cube solver.

## Usage

```python
>>> from rubik.cube import cube
>>> c = cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
>>> print(c)
    OOO
    OOO
    OOO
YYY WWW GGG BBB
YYY WWW GGG BBB
YYY WWW GGG BBB
    RRR
    RRR
    RRR
```

## Implementation

### Piece

The cornerstone of this implementation is the piece class. A piece stores two pieces of information:

1. An integer `position` vector `(x, y, z)` where each component is in {-1, 0,
1}:
    - `(0, 0, 0)` is the center of the cube
    - the positive x-axis points to the right face
    - the positive y-axis points to the up face
    - the positive z-axis points to the front face

2. A `colors` vector `(cx, cy, cz)`, giving the color of the sticker along each axis. For example, a piece with `colors=('Orange', None, 'Red')` is an edge piece with an `'Orange'` sticker facing the x-direction and a `'Red'` sticker facing the z-direction. The piece doesn't know or care which direction along the x-axis the `'Orange'` sticker is facing, just that it is facing in the x-direction and not the y- or z- directions.

Using the combination of `position` and `color` vectors makes it easy to identify any piece by its absolute position or by its unique combination of colors.

A piece provides a method `Piece.rotate(matrix)`, which accepts a (90 degree) rotation matrix. A matrix-vector multiplication is done to update the piece's `position` vector. Then we update the `colors` vector, by swapping exactly two entries in the `colors` vector:

- For example, a corner piece has three stickers of different colors. After a 90 degree rotation of the piece, one sticker remains facing down the same axis, while the other two tickers swap axes. This corresponds to swapping the positions of two entries in the piece’s `colors` vector.
- For an edge or face piece, the argument is the same as above, although we may swap around one or more null entries.

### Cube

The cube class is built on top of the piece class. The cube stores a list of pieces and provides nice methods for flipping slices of the cube, following standard [Rubik's cube
notation](http://ruwix.com/the-rubiks-cube/notation/).

Because the piece class encapsulates all of the rotation logic, implementing rotations in the cube class is dead simple - just apply the appropriate rotation matrix to all pieces involved in the rotation. An example: To implement `Cube.L()` - a clockwise rotation of the left face - do the following:

1. Construct the appropriate [rotation matrix](http://en.wikipedia.org/wiki/Rotation_matrix) for a 90 degree rotation in the `x = -1` plane.
2. Select all pieces satisfying `position.x == -1`.
3. Apply the rotation matrix to each of these pieces.

To implement `Cube.X()` - a clockwise rotation of the entire cube around the positive x-axis - just apply a rotation matrix to all pieces stored in the cube.

### Solver

The solver implements the algorithm described [here](http://www.chessandpoker.com/rubiks-cube-solution.html). It is a layer-by-layer solution. First the front-face (the `z = 1` plane) is solved, then the middle layer (`z = 0`), and finally the back layer (`z = -1`). When the solver is done, `Solver.moves` is a list representing the solution sequence.

The solver averages about 252 moves per solution sequence on 100000 randomly-generated cubes (with no failures). This number can be reduced to about 192 by:

* eliminating full-cube rotations by "unrotating" the moves (Z U L D Zi becomes
L D R),
* eliminating moves followed by their inverse (R R Ri Ri is gone),
* replacing moves repeated three times with a single turn in the opposite
direction (R R R becomes Ri).
