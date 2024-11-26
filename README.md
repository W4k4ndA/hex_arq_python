<h1>Arquitectura Hexagonal en Python</h1>
<p>Este repo solo busca ser una guía de apoyo para todas aquellas personas que ya saben algo de python y quieren incursionar
en las <b>clean arquitectures</b>, concretamente en la arquitectura hexagonal o arquitectura de puertos y adaptadores</p>

<p>Como sabes (o no) conceptos que son comunes en otros lenguajes de programacion como las interfaces, los objetos dinamicos o incluso el tipado de variables
no existen concretamente en python y auqnue se pueden emular, el hacerlo tampoco implica la obligancia o proteccion que conlleva hacerlo como si ocurre en lenguajes
como C# o Java</p>

<p>Si embargo esto no es impedimento para que podamos aplicar arquitecturas limpias en nuestro software escrito en python y disfrutar asi de todos los beneficios
que este tipo de arquitectura nos ofrece y el aprendijae que conlleva el usarla con frecuencia.</p>

<h2>Inspiracion</h2>
<p>Soy programador python y desde hace tiempo he estado estudiando arquitectura de software porque llega un punto en que te das cuenta que aunque tu software
funciona, podria hacerlo mejor o al menos ser mas facil de entender y modificar (sobre todo con esos clientes exigentes o que quieren un software todo en uno)</p>

<p>Fue asi que me tope con el canal en youtube de <a href=https://www.youtube.com/@mvrcoag>MVCO AG</a> un desarrolador full stack mexicano cuya explicacion
de estos de la arquitectura hexagonal es tan clara que fue la primera vez que logre entender los conceptos bien, tanto asi que me inspiro a trasladar su codigo a python.
Aunque el lo explica todo en <b>TypeScript</b> realmente solo se necesita saber un poco de programacion orientada a objetos para poder entender el que, el como y 
el por que de la arquitectura hexagonal.
Este repo bien podria ser un fork del suyo en <a href="https://github.com/mvrcoag/hexagonal-architecture-module-example"><b>https://github.com/mvrcoag/hexagonal-architecture-module-example</b></a>
pero orientado a python en lugar ts y usando <b>Flask</b> en lugar de Express. Asi que vaya para el todo el reconocimiento y los creditos</p>

<h2>Manos a la obra</h2>
<p>Para este ejemplo se crea un modulo de arquitectura hexagonal de Clientes empleando los conceptos que explica marco en su guia de arquitectrua hexagonal. Aunque el
codigo esta comentado para dar el mayor detalle en cuanto al porque se hizo lo que se hizo, si requieres un nivel de explicacion mayor no dejes de ver 
la serie de videos del canal de Marco (@MVRCO AG) en youtube</p>
<p>En primera instancia las interfaces en python no existen como tal, pero si existe el concepto de clase abstracta. Hay un par de maneras de crear una clase
abstracta en python pero se empleo el metodo que implica la importacion del modulo <b>abc</b> y el uso de la clase <b>ABC</b> (Abstract Base Clase) y el 
decorador <b>@abstractmethod</b></p>

<p>
  Dado que python no es compilado no veras ningun mensaje de error indicandote que si implementas las clase abstracta (interfaz en adelante) debes tambien
  implementar sus metodos. Sin embargo al momento de ejecutar el codigo si te dara un error si no implementas los metodos de la interfaz.
</p>
<p>
  Por otro lado debes tener en cuenta que en python todo es un objeto por lo que debes en lo posible mantener esta filosofia.
  Asi mismo, debes evitar a toda costa definir elementos propios de la arquitectura hexagonal como diccionarios. Aunque se parezcan recuerda que los <b>objetos</b> dinamicos
  de javascript o typescript no son iguales a los diccionarios de python (y hago enfasis en objetos porque esa es la clave para enteder la diferencia) principalmente
  porque el diccionario te obliga a hardcodear y no te permite llevar cuenta de los tipos que puede devolver. Para esto existe una solucion: el modulo NameSpaces.
  Este modulo te permite crear objetos "dinamicos" en python (no son dinamicos del todo porque heradan de esta clase pero te permiten definir sus propiedades durante
  la instanciacion de forma declarativa.)
</p>

<p>
  Para la parte del controllador http se utilizo Flask que es un framework web ligero y altamente flexible para python. Lo use porque dentro de los que conozco
  es uno de los mas usados, de los que tiene mayor comunidad y documentacion y creo que es el que mas se puede parecer a Express. Sin embargo no se si Bottle, Pyramid
  o algun otro podria darte un aproach similar. Por su puesto que puedes usar Django que seria el mas grande de todos, pero esa robustes podria ser contraproducente
  para el objetivo que se persigue que es en definitiva la <b>flexibilidad</b>. Ademas debes tener en cuenta que este codigo esta basado en su totalidad en la guia
  de MVRCO AG, por lo que trate de ajustarme todo lo que pude salvando las diferencias no solo de lenguaje si no de conocimientos.
</p>

<h2>Para finalizar</h2>
<p>
  espero que este codigo pueda ayudarte a entender como aplicar los principios de arquitectura hexagonal en python porque conozco de primera mano que practicamente
  no hay contenido donde se explique esto en python o, al menos, donde apliquen la arquitectura usandolo.
  Ciertamente este codigo podria estar mejor, pero al menos puede ser una base para comenzar.
</p>

<p>
  Igualmente estoy desarrollando una aplicacion tipo <b>Pokedex</b> (jajajaja si) que esta inspirada en el proyecto hecho por 
  <a href="https://www.youtube.com/@Linkfydev">Linkfy</a> pero aplicando arquitectura hexagonal (y TKinter en lugar de Flet). Todo esto como un ejemplo de como podrias
  aplicar arquitectura hexagonal en python en una aplicacion un poco mas "real" y viendo como no necesariamente debes tener controladores http si no que en este caso
  sera una aplicacion de escritorio con interfaz grafica.
</p>

<p>En fin, mucho exito para ti y si nadie te lo ha dicho: <b>Sigue asi!, que lo estas haciendo genial </b></p>
<p>Un abrazo</p>
