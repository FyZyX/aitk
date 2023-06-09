Our first Chapter: The Affine Plane
This first chapter is introductory, and has more material in it than any
subsequent chapter! We want to introduce the geometrical framework for
the Algebraic Calculus, which is not Euclidean geometry, but rather the
more flexible geometry of Linear Algebra, namely affine geometry.
Because this may not be familiar to you, we introduce it in an
intuitive, physical fashion via what we call a grid plane, as in the
following diagram:  
![Block of text starting with: Our first Chapter: The Affine Plane](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/parabola1.png?t=1568713523367) 
Hopefully this diagram looks somewhat familiar, but also different! You
can see a parabola with equation $y=x^2$,
but the axes are not perpendicular, and the spacing in the $x$ and $y$ directions are not the
same. We'll show how the basic construction of such a grid plane goes
back to Renaissance artists.

But in addition we will also need a purely algebraic, more formal
definition of the main objects, namely points, lines and vectors that
figure prominently in this geometry. For this we define objects as
certain types of expressions, typically built from numbers, which if not
specified, are rational numbers, and from proportions between
numbers.  

We will in addition be introducing powerful projective coordinates for
points and lines, striking out with novel terminology for dealing
flexibly with vectors and proportions formed by them, connecting with
centres of mass, Archimedes' law of the lever and barycentric
coordinates, and finishing by stating some important classical theorems
of affine geometry. We are overlapping with Linear Algebra here, and
students are encouraged to become familiar with a bit of this subject
(for example through the Wild Linear Algebra video series).  

For first year students: don't be dismayed by the unfamiliar setup and 
the emphasis on definitions. Things will become more comfortable as we
settle into using these ideas further in the course. The geometrical
orientation is an important feature of the Algebraic Calculus, but
ultimately it boils down to just algebra, and mathematics is all about
getting good definitions in the right places.

 $$ 
Affine geometry both informally via pictures, and formally via algebra
$$

We will regard Calculus as a part of *affine geometry*, which is
also the domain of Linear Algebra, and which is built from the
fundamental idea of parallel lines, but without invoking a notion of
perpendicularity. This allows us to compare displacements in the same
direction, but not displacements in different directions. Parallelograms
and midpoints are defined. The fundamental theorems are those of
Menelaus and Ceva, which are best studied in a vector framework, and
connect to Mobius' barycentric coordinates, which are algebraic
generalizations of Archimedes' Law of the Lever.

The basic framework is the *affine plane.* We first introduce this
in an *informal*, geometric way, as a sheet of paper on which we
have built two families of equally spaced parallel lines to form a
**grid plane**, tiling the plane with equal parallelograms.
It is convenient, but not necessary, to use a sheet of graph paper as a
grid plane.

![Grid plane](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/grid.png?t=1568713962631)

But there is also an alternative *more formal algebraic approach*.
This is the framework that we will take to set up our subject correctly.
It is very powerful to have the geometric physical model of a grid plane
at hand while we are developing the more abstract algebraic theory!

 # The informal view of the affine grid plane  

We can create a model for the affine plane geometrically on a piece ofpaper using a square-edge and a prior notion of parallelism, such asgiven by a draftsman's table.  

<img alt="" src="https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/draftsmans_table.jpg?t=1495224013955&amp;t=1495224039036" style="display: block;margin-left: auto;margin-right: auto;max-width: 360px;width: 100%;max-height: 360px"/>

We start by drawing two non-parallel lines, denoted $(x)$ and $(y)$, and called the $(x)$ and $(y)$ axes. Construct two additionallines, each parallel to one of these, called respectively $(x_1)$ and $(y_1)$, so that $(x_1)$ is parallel to $(x)$, and $(y_1)$ is parallel to $(y)$. There is then atechnique, which we call the **Artists' Perspective Rule**(see P1.1.2) to extend these four lines to a grid of equally spacedlines on the paper, extending in all directions, using only parallellines.  

<img alt="" class="img-responsive" data-citation-link="" data-citation-text="" data-long-description="" src="https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/greedWithLines.png?t=1568714010439" style="display: block;margin-left: auto;margin-right: auto;max-width: 404px;width: 100%;max-height: 277px"/>

The lines are labelled with integers, but rational values are not hard toinsert if needed, and with this framework we can both visualize andspecify points and lines: the former in terms of $(x)$ and $(y)$ coordinates, the latter in terms of linear equations in $(x)$and $(y)$.  

It is understood that even though the paper has a limited finite extent,it can, in principle, be extended in any direction, and that lines drawnon it can also be extended. This is the same convention that Euclidadopted and that will be repeated in other places as we develop thecalculus: we are able to extend a given picture, but do not make anygrandiose claims about such extensions "going on to infinity" or somesuch. We work with what we can write down.

 The Artist's Perspective Rule  

Renaissance artists developed the technique to draw realistic perspective images of tiled floors, generally in a projective setting, where there is an implicit horizon, or "line at infinity". In this case, they replaced the notion of "parallel lines" with the notion of "lines meeting at a point on the horizon".

![A tiled floor with some tiles skewed to appear as converging](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/Tile_Floor_1280px-Paolo_Uccello_062.jpg)

 # Integer coordinates 

We pick a distinguished axis from each of the two families of equally  
spaced parallel lines, and label them as the $x$ and $y$ axes. We sometimes, rather 
arbitrarily, call the direction of the $x$  
axis **horizontal**, and the direction of the $y$ axis **vertical**. In this case, all the lines parallel to the  
$x$ axis are also called  **horizontal**, and all the lines parallel to the $y$ axis are also called
**vertical**. The point where the $x$ and $y$ axes meet is called the  
**origin**, and we denote it by $O$. 

We specify a particular direction on each of the axes, and use that to  
mark off the meets as $0,1,2,3$  
and so on, with $0$  
corresponding to the origin $O$.
In the other direction, we mark off points labelled $-1,-2,-3$ and so on. Thus, on
both of the axes, the meets with the other family are labelled with
integers, and every such meet corresponds to exactly one such integer.  

The meet of the vertical line which meets the $x$ axis at the integer marked  
$m$ and the horizontal line 
which meets the $y$ axis at the
integer marked $n$ will be 
denoted $[m,n]$. This is an 
(affine) point in this geometric informal setting.

<img alt="" class="img-responsive" data-citation-link="" data-citation-text="" data-long-description="" src="https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/greedWithMN.png?t=1568714049705" style="display:block;margin-left:auto;margin-right:auto;max-width:417px;width:100%;max-height:294px;"/>

We see that the plane that we so construct is similar to the usual $x-y$ plane in high school, except  
that the orientation of the horizontal and vertical lines may be  
somewhat askew, that the scales on the two coordinates $x$ and $y$ axes are not the same, and 
that so far, we only have integral points. In particular, we do not have  
a well-defined notion of perpendicularity, and also not of length. But  
we are able to compare displacements in a particular direction, and we  
do have a rudimentary notion of area, as the plane is now subdivided, or  
partitioned, into equal-sized parallelograms.

 $$Rational coordinates$$ 

We may also consider $m$ and  $n$ above to be rational numbers.  Consider, for example, the segment of the $x$-axis consisting of points $[0,\lambda]$, $0\le \lambda\le 1$. To visualise an arbitrary rational number $\frac{M}{N}$ is this segment  for integers $N,M$ on this axis we may subdivide this segment into $N$ equal pieces  and take $M$ of them. Let's, for example, take $M=5$, $N=6$ to mark $\frac{5}{6}.$  

![](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/fractions.png?t=1568714085487)

Using this method, we may mark any rational number on $x$ and $y$ axis. For two rational numbers $r,s$ the meet of the vertical line which meets the $x$ axis at the point marked $r$ and the horizontal line which meets the $y$ axis at the point marked $s$ will be denoted $[r,s]$. The diagram below shows the point $[\frac{5}{6}, \frac{3}{2}]$.

![](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/fractions2.png?t=1568714116733)

 ## The formal view of the modern Affine Plane: key definitions

When we proceed formally in geometry, we are motivated by our geometric
intuition and pictures as above, but we aim to have the concepts defined
purely algebraically, independent of any assumptions on the nature of
space. Hopefully, the theory that we build algebraically and rigorously
will mirror the geometric and physical intuition that we gain by drawing
diagrams and performing experiments!

The modern approach to setting up the affine plane is to use an
underlying number system---for example the rational numbers---to define
points and lines, and then to prove the required properties of them
algebraically. We now introduce the main definitions that will be needed
for us (this is not a course in affine geometry, so we do not pretend
that this is a complete introduction to the subject). More of the
logical connections will be explored in the Problems and Questions.

A **point** $A=[r,s]$ is an ordered pair, or
2-list, of rational numbers. Our convention is that order is denoted by
a comma, and that the square brackets alert us to repetitions being
allowed. In this course, points will be denoted with capital letters.
The **origin** is the special point $O=[0,0]$.

A **line** $\ell$ is
an equation of the form $ax+by=c$, a linear equation
in $x$ and $y$, where $a,b$ and $c$ are rational numbers with
$a$ and $b$ not both zero, and where
$x$ and $y$ are variables, or simply
letters. To represent the line we will write
$$\ell : ax+by=c.$$

We will allow alternate forms obtained by rewriting this equation. If $b$ is not equal to $0$, then we may write 
$$\ell : y=-(a/b) x+c/b.$$ If $a$ is not equal to $0$, then we may write
$$\ell : x=-(b/a) y +c/a.$$ We may also sometimes write
$$\ell : ax+by-c=0$$ 
or putting the lower order terms first,
$$\ell : -c+ax+by=0.
$$
We will say that the point $A=[r,s]$ **lies on**
the line $\ell : ax+by=c$
precisely when $ar+bs=c.$ In
this case we also say that the line $\ell$
**passes through** the point $A,$ or that $A$ and $\ell$ are
**incident**. Then any two distinct points $A$ and $B$ determine a unique line
$AB$ which passes through them
both, called their **join**.

Three or more points are called **collinear** precisely when there is a line that passes through all these points.

Define two lines $\ell:ax+by=r$ and $m:cx+dy=s$ to be **parallel **(notation: $\ell||m$) precisely when $ad-bc=0$.

Sometimes we will also distinguish two types of parallel lines. Observe
that the expression $ad-bc$
appearing in the definition of parallel lines is in fact the determinant
of the matrix $$\left(\begin{array}{cc} a &b\\c&d\end{array}\right).$$  We know from linear
algebra that if the determinant is zero then the system $\left\{\begin{array}{l}ax+by=r \\
cx+dy=s\end{array}\right.$ has no solutions, or the solution
is a one-parameter family
(line). In the case when there are no solutions, we say that two lines
$\ell$ and $m$ are parallel and **distinct **(notation:
$\ell\neq m$). In the case when
there is a one-parameter family,
we say that the lines are parallel and **coincident**
(notation: $\ell= m$). 

When two lines $\ell:ax+by=r$ and $m:cx+dy=s$ are not parallel, that is $ad-bc\neq 0$,
the system above has a unique solution, which determines a unique point denoted as $\ell m$ and called
the **meet** of these two lines.

A **parallelogram** is a quadrilateral $\overline{ABCD}$ for which $AB$ and $CD$ are parallel distinct lines,
and also for which $AD$ and $BC$ are parallel distinct lines. The lines $AC$ and $BD$ are called the **diagonals**
of the parallelogram.

If $A=[r,s]$ and $B=[t,u]$ then the **midpoint of** $A$
**and** $B$ is the point 
$$M=\left[\frac{r+t}{2},\frac{s+u}{2}\right] $$.

# Visualizing points and lines

Given a point such as $[\,2,1\,]$, we
can represent it visually on an affine grid plane by placing a small dot
where the lines $x=2$ and $y=1$ meet, as shown. This
diagram also shows the line $2x-y=3$ which passes through
the point $[\,2,1.\,]$

![line1](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/line1.png?t=1568714149808)

Of course, a line passes through many points! In order to draw a line
accurately, it is usual to graph at least two points on it. Here is the
line $3x-2y=6$ with four points
which lie on it, namely $[\,0,-3\,],
\left[1,-\frac32\right], [2,0]\,\right]$ and $\left[\,3,\frac32\right.\,]$. Note
that the second point here is the midpoint of the first and third, and
the third is the midpoint of the second and fourth.

![line2](https://www.openlearning.com/courses/algebraic-calculus-one/points_and_lines_in_the_affine_plane_videos/line2.png?t=1568714179391) 

Please remember that such a visual representation of a line is only
partial and approximate: we agree that the page can, in principle, be
extended, and so the line can also be extended, and further points on it
shown. And we will agree that different grid planes are equally valid in
picturing our formal setup of algebraic points and lines: in particular,
we will not require "perpendicular" axes, and "equal lengths in
different directions", and we cannot refer to "angles" between lines. In
affine geometry such metrical notions play no role.

 2-proportions and 3-proportions
Implicit in the definition of line is the idea that the equation is essentially unchanged when all coefficients are multiplied by the same (non-zero) number. Thus, \(3x-y=2\) represents exactly the same line as \(12x-4y=8\). We want to introduce some terminology that allows us to efficiently express this important idea, and that will lead to the useful projective forms for describing both points and lines in our next module.  

A **2-proportion** is an expression of the form \(a:b\) where \(a,b\) are numbers, not both zero,
subject to the convention that 
$$a:b=c:d$$ precisely when $$ad-bc=0.$$ This is a lot like
equality of fractions. By multiplying both numbers in a proportion by 
the same non-zero scalar, or number, the proportion does not change.
Thus, the two proportions \(3:4\)
and \(6:8\) are equal. So are the
proportions \(5:0\) and \(-\frac{7}{2}:0\).  

A **3-proportion** is an expression of the form \(a:b:c\) where \(a,b,c\) are numbers, not all
zeros, subject to the convention that   

$$a:b:c=d:e:f $$ precisely when  
$$ae-db=af-cd=bf-ce=0.$$   If
the 2-proportions $$a:b,\quad a:c, \quad
b:c$$ are defined, the condition \(a:b:c=d:e:f \)  is 
the same as the condition  \(a:b=d:e\)
and \(a:c=d:f\) and \(b:c=e:f\). Thus, the two
proportions \(3:4:5\) and \(6:8:10\) are equal. So are the 
proportions \(5:0:-1\) and \(-\frac{1}{2}:0:\frac{1}{10}.\)  

We now see that two lines \(\ell:ax+by=r\) and \(m:cx+dy=s\) are parallel precisely
when \(a:b=c:d\).  

Proportions capture the relative sizes between two objects, while numbers 
capture absolute sizes. The ancient Greeks appreciated that in many
situations, relative sizes were more relevant than absolute sizes!  

The following result shows that the notion of a proportion is an  *equivalence
relation*.

 **Proposition** For any 2-proportions \(a:b,c:d\) and \(e:f\) we have

1. \(a:b=a:b\)

2. If \(a:b=c:d\) then \(c:d=a:b\) 

3. If \(a:b=c:d\) and \(c:d=e:f\) then \(a:b=e:f\).


# Relations between 2-proportions and fractions 

A 2-proportion \(a:b\) is very close to a fraction \(\frac ab\)  since equality of proportions $$a:b=c:d$$ and equality of fractions \begin{equation*} \frac ab=\frac cd \end{equation*}  in both cases amounts to the condition $$ad-bc=0.$$ However there is an important distinction that prevents the usual arithmetic of fractions being readily adopted for 2-proportions: for a 2-proportion \(a:b\) we require at least one of \(a,b\) to be non-zero, while for a fraction \(a/b\) we require \(b\) to be non-zero.