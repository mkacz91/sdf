* [ ] Abstract

### Introduction

_This section contains most related work references_.

* [ ] What is a vector texture and why use it.
* [ ] Coverage vs SDF. Image comparisons with explanation of artifacts.
* [ ] Currently available methods for SDF computation.
* [ ] How different SDF radius and precision affect the resulting image. Setting goals.
  
### Theorethical overwiew

* [ ] General idea. Reconstructing SDF from multiple coverages.
* [ ] How rasterization on GPU works and how it translates to our method.
* [ ] Derivation of transformations needed to obtain specific coverages.
* [ ] Coverage formula.
* [ ] Derivation of the reconstruction maps.

### Implementation

* [ ] Rendering of complex shapes using stencil buffer.
* [ ] Overview of sample-based antialiasing and how it affects precision of the method.
* [ ] Reconstruction map as dependent texture lookup.
* [ ] Reconstruction map as approximating polynomial.
* [ ] Pseudo code for a naive method (without resource considerations).
* [ ] Evaluation.

### Practical application

_The thesis will ship with a library and command line tool that generates SDF representation
of glyphs in a font file._

* [ ] Efficient resource utilization.
* [ ] Geometry processing. Primer on Bezier curves.
* [ ] Parallelization considerations.
* [ ] Pipeline design.
* [ ] User guide.
* [ ] Performance evaluation



