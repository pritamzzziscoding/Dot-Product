# Dot Product Using Python

## Tables of Contents

- Defination
  - General
  - Algebraic
- Mathematical Formula
- Geometrical Meaning
- Application Table
- Vectors in Numpy

## Definations
<ins>**General Defination :**</ins> In mathematics, the __*dot product*__ or __*scalar product*__ is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors), and returns a single number.

>It is often called the inner product.

<ins>**Algebric Defination:**</ins> Algebraically, the dot product is the sum of the products of the corresponding entries of the two sequences of numbers.

## Mathematical Formula
Let two vectors be **a** and **b** then Their Dot Product is :

$$\text{\textbf{a}.\textbf{b}}= \sum_{i=1}^{n} a_i  b_i = a_1b_1 + a_2b_2+ \ldots a_nb_n$$

## Geometrical Meaning
In Euclidean space, a Euclidean vector is a geometric object that possesses both a magnitude and a direction. A vector can be pictured as an arrow. Its magnitude is its length, and its direction is the direction to which the arrow points.

The magnitude of a vector **a** is given by $||a|| = \sqrt{a_1^{2} + a_2^{2} + \ldots a_n^{2}}$ which is also known as Euclidean Norm

<img style="background-color: white" src="./Inner-product-angle.svg.png" alt="This will be an image" height="200">


## Application Table
| Domain | Use |
| --- | --- |
| **Physics** | Used to denote various physical quantities like displacement |
| **Maths** | Used to analyse the 3-D system |

> [!TIP]
> The dimension of a vector can also be greater than 3

> [!IMPORTANT]
> Vectors are very important in ML and DL

> [!WARNING]
> Never avoid vectors


## Vectors in Numpy
In order to access vectors in python use the Numpy[^1] library

```
import numpy as np

a = np.array([1,2,3])
```
This will simply create you an vector.

[^1]: It is a library in python for mathematical Manipulation. For more info read [Numpy Documentation](https://numpy.org/doc/) 






