---
title: "Data science como producto"
date: "2025-03-04"
summary: "Una guía corta para desarrollar data science desde un approach de producto"
description: "Re-pensar todo proyecto de data science como un producto nos va a mantener siempre cerca del impacto."
toc: false
draft: false
readTime: true
autonumber: true
math: true
tags: ["productos"]
showTags: false
---

He desarrollado una buena cantidad de proyectos de data science, y pucha que fácil es diverger del camino que nos lleva al éxito.
¿Cuál es ese éxito te preguntarás? Un clásico, agregar valor. No importa cómo, pero que lo que se estaba haciendo antes de alguna forma, 
ahora se esté haciendo mejor, y que eso traiga consecuencias positivas al entorno 
(eg. aumentando eficiencia usemos menos recursos, o usemos mejor los recursos que ya tenemos). Suena fácil, pero aparte de la solución en sí misma, 
hay que acordarse que adoptar mecanismos que no entendemos es re difícil. No queremos hacerlo, no queremos sufrir de más. Es como tener que disparar 
esas super pistolas de _Men in Black_: prefiero mil veces una menos colorinche y con menos berrinche pero que haga la pega y no me falle. También
hay personas que prefieren de primera las pistolas de _Men in Black_ y podrían decir: "_qué tipo conservador! vamos por lo más coool_". Y eso está bien. 
Disparar un rato esas pistolas y jugar con ellas puede ser bacán. Pero ¿me llevaría una de esas tremendas cosas a una pelea real? Tal vez sí, si fueran 
más livianas, si las supiera arreglar yo sólo, si fueran un poco más chicas. Por eso acá digo, lleguemos allá construyendo desde lo más simple, y pensemos
como si fuesemos ese usuario final.

Para no generalizar hablaré por mí. En estos casos, mi mayor enemigo es _la complejidad_. Pareciera que mientras algo es más complejo, es mejor. 
Para mi, la complejidad por sí misma sostiene cierta belleza que me atrae e hipnotiza un poco. Es _sexy_. Pero la verdad, es que la complejidad no
se sostiene por sí sola, y hay que llamarla cuando se le necesita. 

Por otro lado, existe como cierta verguenza a mostrar cosas simples que funcionan. Es como si uno quedara expuesto al _trolleo_ público 
de otro que lo puede hacer mejor. Hoy en día padecemos de este mal en que todos los ejercicios se transforman en una compentencia. Prefiero
no caer en eso, y hacer cosas simples sin verguenza. 

Ahora, si la _cosa_ simple no alcanza, claro... hay que llamar a la señora _complejidad_.



## Introduction

sasasassa

This results in a list of non-overlapping tables, meaning we likely search only in one of them during a query.
For instance, given the following three tables, ordered by flushing time:

- $t_1 = [ a : 1, b : 2 ]$
- $t_2 = [ b : 7, c : 3 ]$
- $t_3 = [ a : 9, d : 9 ]$


The result after a sorted run where the max table size is 3 will be [^3]:
$$\text{sorted run} = [a:10, b:20, c:30], [d:50, z:100]$$

This process is triggered periodically by a background thread, 
we fix a maximum size for each level in the SST list and, if the size exceeds this limit, 
we perform a sorted run merging level $l$ with $l + 1$. Level and SST max sizes increase by a factor of $1.75$ on each level.

Merging the SSTables in a single sorted iterator is equivalent to the problem of merging $k$ sorted iterators.
The problem can be solved by using a priority queue to find the next element in $log(k)$ time complexity. [^4]

[^3]: Note that in reality we focus on byte size and not number of elements.
[^4]: If you want to give this task a try, here's an equivalent [Leetcode problem](https://leetcode.com/problems/merge-k-sorted-lists/).

## Conclusions

Overall this was a really fun project, there were far more implementation
challenges than I expected and some cool DSA concepts came up here and
there during the design.

There is a lot that could be done to improve the project, skip lists could
be optimized further, bloom
filters could be made more cache efficient, and proper crash recovery could
be implemented. I'll perhaps update the code in the future.

Thank you for reading this far, feel free to get in touch for suggestions or clarifications!

Have a nice day 😃


### References

- [Designing Data-Intensive Applications](https://dataintensive.net/)
- [Database Internals](https://www.databass.dev/)
- [A Skip List Cookbook](https://api.drum.lib.umd.edu/server/api/core/bitstreams/17176ef8-8330-4a6c-8b75-4cd18c570bec/content)
