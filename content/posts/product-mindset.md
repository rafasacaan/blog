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
(eg. aumentando eficiencia usemos menos recursos, o usemos mejor los recursos que ya tenemos). 

Suena fácil, pero aparte de la solución en sí misma, 
hay que acordarse que adoptar mecanismos que no entendemos es re difícil. No queremos hacerlo, no queremos sufrir de más. Es como tener que disparar 
esas super pistolas de _Men in Black_: prefiero mil veces una menos colorinche y con menos berrinche pero que haga la pega y no me falle. También
hay personas que prefieren de primera las pistolas de _Men in Black_ y podrían decir: "_qué tipo conservador! vamos por lo más coool_". Y eso está bien. 
Disparar un rato esas pistolas y jugar con ellas puede ser bacán. Pero ¿me llevaría una de esas tremendas cosas a una pelea real? Tal vez sí, si fueran 
más livianas, si las supiera arreglar yo sólo, si fueran un poco más chicas. Por eso acá digo: lleguemos hasta allá construyendo desde lo más simple, y pensemos
como si fuesemos ese usuario final.

Para no generalizar hablaré por mí. En estos casos, mi mayor enemigo es _la complejidad_. Pareciera que mientras algo es más complejo, es mejor. 
Para mi, la complejidad por sí misma sostiene cierta belleza que me atrae e hipnotiza un poco. Es _sexy_. Pero la verdad, es que la complejidad no
se sostiene por sí sola, y hay que llamarla cuando se le necesita. 

Por otro lado, existe como cierta verguenza a mostrar cosas simples que funcionan. Es como si uno quedara expuesto al _trolleo_ público 
de otro que lo puede hacer mejor. Hoy en día, padecemos de este mal en que todos los ejercicios los transformamos en una competencia. Prefiero
no caer en eso, y hacer cosas simples sin verguenza. 

Ahora, si la _cosa_ simple no alcanza, claro... hay que llamar a la señora _complejidad_.

## Introducción

El objetivo es lograr cambiar nuestro _approach_:
- **"simplemente resolver problemas técnicos"** ❌
- **"crear productos que entreguen valor real"** ✅
  
Pensando como un _product developer_ desde el día uno podremos **conectar** nuestro trabajo directamente con las necesidades de un usuario (para hacerlo más real y acentuar las ganas que tenemos de generar impacto, entiéndase mejor como las necesidades de una _persona_).

## Descubriendo el problema

Primero, necesitamos entender **a quién** estamos ayudando. 

No es la organización, no es el stakeholder, no es el champion. Encontremos quién es! Preguntémosle su nombre, conozcámoslo, conversemos con esa persona. Acompañémoslo una mañana entera. Seamos su sicólogo por un rato, y entendamos los dolores que tiene, y también sus éxitos. Imaginemos se llama Roberto.

Si nos preguntan qué estamos haciendo, nuestra respuesta nunca puede ser: "Estoy construyendo un modelo de _churn_". En realidad estamos 
ayudando a identificar usuarios en riesgo de irse de la compañia, a los cuáles queremos intentar retener. Eso se _puede_ hacer con un modelo de _churn_. Pero también se puede hacer de mil formas más. También necesitamos encontrar una forma en que Roberto pueda interactuar con _la cosa_. También
necesitamos integrar _la cosa_ con los sistemas de Roberto. También necesitamos que Roberto tal vez puede identificar fallas de _la cosa_, 
para que esta pueda evolucionar en el tiempo, y construir sobre ella. 

Esta lista de cosas es bastante más que sólo un modelo de _churn_, y ayuda a hacer el _mind shift_ de producto que buscamos.

En resumen, algunas preguntas importantes acá son:
- ¿Quién usará esta herramienta y cómo?
- ¿Qué decisiones mejorarían si tuvieramos mejores _data insights_?
- ¿Cómo se vería un escenario de éxito para el usuario?

Segundo, diseñemos **métricas** correctas para medir el éxito. Más que reportar que _la cosa_ tiene un accuracy del 92%, midamos en qué porcentaje estamos mejorando el _churn_, o cuál es el porcentaje de _churn_ mensual que buscamos/medimos.

## Diseñando la solución





