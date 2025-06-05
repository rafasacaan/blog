---
title: "Data science como producto"
date: "2025-03-04"
summary: "Una guía corta para desarrollar data science desde un approach de producto"
description: "Re-pensar todo proyecto de data science como un producto nos va a mantener siempre cerca del impacto."
toc: false
draft: true
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

De esto ya se ha escrito bastante, pero quería registrarlo a mí manera, sin inspirarme en ningún otro artículo. Creo que eso le agrega _ortogonalidad_ al tema y a la web.

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

No es la organización, no es el stakeholder, no es el champion. Encontremos quién es! Preguntémosle su nombre, conozcámoslo, conversemos con esa persona. Acompañémoslo una mañana entera. Seamos su sicólogo por un rato, y entendamos los dolores que tiene, y también sus éxitos. Imaginemos que se llama Roberto.

Si nos preguntan qué estamos haciendo, nuestra respuesta nunca puede ser: "Estoy construyendo un modelo de _churn_". En realidad estamos 
ayudando a Roberto. Estamos ayudando a identificar usuarios en riesgo de irse de la compañia, a los cuáles queremos intentar retener. Eso se _puede_ hacer con un modelo de _churn_. Pero también se puede hacer de mil formas más. También necesitamos encontrar una forma en que Roberto pueda interactuar con _la cosa_. También
necesitamos integrar _la cosa_ con los sistemas de Roberto. También necesitamos que Roberto tal vez puede identificar fallas de _la cosa_, 
para que esta pueda evolucionar en el tiempo, y construir sobre ella. 

Esta lista de cosas son bastante más que sólo un modelo de _churn_, y ayuda a hacer el _mind shift_ de producto que buscamos.

En resumen, algunas preguntas importantes acá son:
- ¿Quién usará esta herramienta y cómo?
- ¿Qué decisiones mejorarían si tuvieramos mejores _data insights_?
- ¿Cómo se vería un escenario de éxito para el usuario?

Segundo, diseñemos **métricas** correctas para medir el éxito. 

Más que reportar que _la cosa_ tiene un accuracy del 92%, midamos en qué porcentaje estamos mejorando el _churn_, y cuál es el porcentaje de _churn_ mensual que buscamos/medimos.

## Diseñando la solución

Una vez identificado el problema y el usuario, dibujemos (sí, literalmente) la navegación o el **_journey_ de ese usuario** a través de _la cosa_, de principio a fin.

Por ejemplo, _"Roberto abre su dashboard el lunes a.m. y ve una lista priorizada de cuentas, cada una con sus factores de riesgos subrayados"._
Necesitamos entonces sentarnos a dibujar estos recorridos y representarlos a través de frases simples. El objetivo es **tener una colección de frases que construyan e viaje**, y entender que esto no lo hacemos solos ni para nosotros, sino que para ayudar a Roberto. Pregúntemosle a Roberto si este viaje le parece y qué comentarios tiene. Y los consideramos, e iteramos.

El enemigo acá se llama _ansiedad_. No queremos resolver toda de una sola vez. No queremos viajes que sean como árboles con ramas y ramas de las ramas. Queremos lo esencial, ese 80/20 que ya nos posiciona en hacer algo distinto y que queremos _testear_. Esta resistencia a las ramificaciones se llama **MVP** o  _Minimum Viable Product_. Con el _MVP_ hacemos dos cosas:

- Encontramos y **definimos las funcionalidades básicas** que juntas hacen que _la cosa_ sea una cosa, y no una suma de _features_ revoloteantes. Y asegurémosnos que la _cosa_ también sea una _cosa nueva_ que agregue valor. 
- Recolectamos **_feedback_** del usuario. Nunca nos olvidamos que trabajamos para Roberto, nuestro ahora amigo.

Acá nos podemos hacer las siguientes **preguntas de scope**:
- ¿Cómo se vería la solución más simple que agrega valor?
- ¿Cuál es la pregunta más importante que queremos responder?
- ¿Cuales son los benchmarks mínimos que necesitamos satisfacer?
- ¿Podemos entregar valor con los datos/recursos que tenemos?
- ¿Qué restricciones existen?
- ¿Existe soluciones baseline que podamos apalancar?

Y **preguntas técnicas**:
- ¿Tenemos suficientes datos para crear un modelo inicial robusto?
- ¿Podemos procesar por batches y luego en tiempo real?
- ¿Qué deudas técnicas podemos comprometer con tal de desarrollar rápido?
- ¿Cómo evaluamos el funcionamiento técnico del approach (eg. tiempos de respuesta)?

Si necesitamos desarrolar en equipo, tambien **preguntas estratégicas**:
- ¿Cuál es el timeline que tenemos?
- ¿Cuál es la forma más rápida de llegar a los usuarios para obtener feedback?
- ¿Qué aprendizajes queremos obtener de este _MVP_?
- ¿Qué métricas _trackearemos_?
- ¿Cómo incorporaremos el _feedback_ de usuario?

Y no olvidemos de **mitigar riesgos**:
- ¿Cuales son los supuestos o los _unkowns_ de nuestro approach?
- ¿Qué pasa si _la cosa_ se desempeña bajo lo esperado?
- ¿Hay consideraciones éticas que necesitamos respetar?
- ¿Cuál es el _fallback plan_ si el _MVP_ no funciona?
- ¿Cómo comunciaremos las limitaciones del _MVP_ a los stakeholders?

Por último, queremos planificar el **deployment y adopción**:
- ¿Cuál es la forma más simple de integrar _la cosa_ a los _workflows_ actuales?
- ¿Quiénes tienen que estar involucrados en probar el _MVP_?
- ¿Qué soporte necesitarán los usuarios (eg. documentación, manual, talleres)?
- ¿Cómo obtenemos _feedback_ estructurado desde los usuarios?
- ¿Qué haría que los usuarios quieran seguir usando esta solución?

## Arquitectura tech

En este paso, necesitamos pensar en los huesos o los fierros que darán soporte para _parar_ nuestro producto. Es importante tener una visión de largo plazo, que sea flexible y ágil para escalar y absorber modificaciones. Que funcione hoy, y escale mañana.

Algunos puntos a considerar para la arquitectura considerando número de usuario y tmamaño de datos son:
- Frecuencia de actualización de los datos
- Dónde y cómo sera _deployeada_ la solución
- Puntos de integración con sistemas existentes
- Dependencias técnicas y limitaciones

_Pro tip_: documentar las decisiones y su razonamiento para poder compartirlas con los equipos técnicos.

## Desarrollando el producto

Si queremos ser ágiles, trabajemos _agile_ (sí, es obvio). Planificar y compartimentar (así se dice?) el trabajo en ciclos de 1-2 semanas. Cada ciclo cumple una misión, y está compuesto por una colección de tareas. Después de cada ciclo, se comparten los progresos con los stakeholders para validar que estamos en el camino correcto. Si noes así, la idea es absorber rápido lo que necesitamos incluir mediante un plan para el _sprint_ siguiente. 

Una máxima: **crear prototipos rápido para _testear_ supuestos críticos**. Mock-ups, dashboards, lo que sea pero tiene que ser rápido para reemplazar la imaginación por una cosa única sobre la que podamos opinar y construir. 

Un recordatorio: **colaborar _cross_-discipplinas**. Necesitamos conectarnos con la gente de datos, infraestructura, diseño y negocio. Y Roberto, por supuesto.

Durante todo el proceso de desarrollo, es importante tener un ojo puesto en el horizonte, donde _trackeamos_ las métricas que nos importan y vamos registrando nuestros avances cuantificables y cuantitativos.

## Medición e iteración

Una vez implementado nuestro _MVP_, la misión es doble:
- **Monitorear** (métricas, comportamientos, evaluación de usuario, impacto en el negocio)
- **Mejorar** (planificar modificaciones o nuevos features, priorizando por potencial impacto)

Y repetir.

## Conclusión

Cuando empiezas a ver tus proyectos de datos como si fueran productos, estás cambiando el juego. Ya no es solo códigos y modelos complicados - estás creando algo que realmente sirve y que la gente quiere usar. Con este enfoque, tu trabajo técnico se convierte en herramientas útiles que resuelven problemas reales y que la gente valora. Al final, lo que importa no es lo complejo que sea tu análisis, sino que alguien lo use y tenga una buena experiencia haciéndolo.




   


  





