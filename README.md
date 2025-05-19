# **ParticipoMX** 

# **Voto descentralizado, encriptado, encadenado y participativo**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdp43xD5tmyU_WewnrNjmlY5FdruU2pUJ00ngcZ0D9RyaYOTNegtobezwwfrL7Vq4xdCVpimlFcbgqu8F6mJiWXwwNYnIg3fkYYzGGQrsnQ73GIUuF_pPfUjqRVEVN8QJ4hF5aBdTlcaDVny-1GsQj4R618?key=bmTiORLivl5REObwqZ86Hw)


Licenciatura en Ciencia de Datos para Negocios

José Adán Quintero Sánchez - 401 MAC


# Índice

Glosario………………………………………………………………………………………………………………..………3

Introducción………………………………………………………………………………….……………………………..4

¿Qué es el voto encriptado?...................................................................................................11

¿Cómo se encadena?...............................................................................................................16

¿Cómo es la boleta digital?.....................................................................................................18

Ésta propuesta……………………………………………………………………………………..…………………….19

Demo……………………………………………………………………………………..………………………..19

Código abierto……………………………………………………………………..………………………….19

Baúl Temporal…………………………………………………………………………..…………………….20

Cálculo de Rentabilidad………………………………………………………..…………………………21

Diagrama de topología de red P2P……………………………………..…………………………..21

Predicción de participación (Comicios 2024)...........................................................22

Capturas de App ParticipoMX………………………………………………………………….………………….26

Impresión Remota del voto………………………………………………………………………………………..31

Encriptación del voto………………………………………………………………………………………………….33

Tablero de votos en Tiempo Real……………………………………………………………………………….34

Diagrama de App ParticipoMX……………………………………………………………..…………………….37

Emulación padrón electoral (Google Colab 143,239 registros creados)..........................38

Conclusión…………………………………………………………………………………………………………..……..41

Bibliografía……………………………………………………………………………………………………..…………..43


#

# Glosario

**Hash**: Cadena de texto encriptada

**Encriptado**: Convertir el contenido de un mensaje en otro código para que pueda ser leído o interpretado en otro

**OLD**: Observador electorales de Larga Duración

**OCD**: Observador electoral de Corta Duración

**Token**: Código único proporcionado por el administrador de la aplicación

**Pen-Testing o pentesting**: _Penetration Testing_ (Pruebas de seguridad contra hackeo)

**QR**: Quick Response

**Dashboard**: Tablero con gráficos para inferencias estadísticas 

**Persistencia Políglota**: Se refiere a la utilización de distintas arquitecturas para el manejo de los datos, refinamiento, análisis, almacenamiento y visualización de los mismos 

**P2P**: Se refiere a una red descentralizada de igual a igual que permite transacciones seguras y privadas utilizando protocolos criptográficos donde las personas interactúan entre sí utilizando una plataforma P2P como Cryptomus, y esas interacciones definen qué es P2P y cómo funciona.


# Introducción

El panorama actual del proceso de votaciones electorales a nivel mundial ha evolucionado notablemente en los últimos 15 años. El acceso a nuevas tecnologías como _smartphones_ se ha generalizado en gran parte del mundo.

Se puede entender que tras este cambio de hiperconectividad se desarrollan e implementan nuevas formas de participar en consultas ciudadanas, tomando en cuenta aspectos como la movilidad y la reducción de emisiones de contaminación. 

En este caso específico, para los comicios sexenales de elecciones presidenciales en México, país donde ya existen sistemas de voto electrónico a través de urnas electrónicas diseñadas específicamente para ello. Sin embargo la brecha para el marco legal ha impedido casi en su totalidad su funcionamiento.

La necesidad es evidente y se requiere de un proceso electoral que garantice una elección segura y confiable, impidiendo, suplantación de votos, duplicidad, destrucción y/o robo de casillas.

**Un proceso electoral con tecnología criptográfica encadenada y descentralizada** ofrece: 

1. **Accesibilidad**

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Perspectiva electoral**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Infraestructura**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Poder votar a través de un smartphone o una computadora brinda un alcance excepcional.Mediante una aplicación digital más personas pueden participar en el proceso electoral, incluso aquellos que no pueden asistir físicamente a los centros de votación. Esto amplía la participación y asegura que aquellos con horarios ocupados o que se encuentran lejos de su lugar de votación tengan una oportunidad igual de ejercer su derecho al voto.Además, la comodidad de **poder votar desde cualquier ubicación y en cualquier momento** aumenta la conveniencia para los ciudadanos, lo que a su vez fomenta una mayor participación en el proceso democrático****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd6PCctO4X16xcuRqSc-c3W6WRbQrzHMgOx3MKWK2aC4En88tNDssLP0VMnNiYEeklUB44c-WX7VjhW6mEpXJkmbPT04ouh0iook6rAIwEx9870ouvwYyjtAV1Qhl_1MbGaYpc1eBQWBoMka4SebnbKIS0?key=bmTiORLivl5REObwqZ86Hw)**** | Una aplicación desarrollada en **Python** nos brinda la facilidad de contar con los mejores algoritmos de encriptación elíptica (computacionalmente imposibles de descifrar) y encadenamiento que también puede ser una aplicación nativa (iOS, Android, OS X, Linux o Windows) o directamente una aplicación web gracias a la flexibilidad y versatilidad de este lenguaje de programación.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7TcRfsAr2vYQR_gsM0QRdQ0kAfAFbTOClz2gAssKsTNi1eM1WFfyiPckv9htiTpG-9yICf-RWgy3bBnIAqOWOjk352rzspqQs4jsr1gBWAbzeaX1Si2oNJO-71X6CDbSkTbH-JCvtWgGKSF7DaK94jlY?key=bmTiORLivl5REObwqZ86Hw)Además de contar con miles de librerías para hacer inferencias estadísticas, predicciones, regresiones lineales, de aprendizaje de máquina e inteligencia artificial.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7TcRfsAr2vYQR_gsM0QRdQ0kAfAFbTOClz2gAssKsTNi1eM1WFfyiPckv9htiTpG-9yICf-RWgy3bBnIAqOWOjk352rzspqQs4jsr1gBWAbzeaX1Si2oNJO-71X6CDbSkTbH-JCvtWgGKSF7DaK94jlY?key=bmTiORLivl5REObwqZ86Hw) |

2. **Seguridad** 

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Perspectiva electoral**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Infraestructura**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Al acceder a la aplicación mediante tu **llave pública de tu credencial INE** (QR trasero), una confirmación **biométrica de tu rostro** (reconocimiento facial), tu intervención humana de ingresar datos y confirmarlos mediante correo, SMS o WhatsApp, garantiza la integridad del proceso para verificar la identidad de cada elector y así evitar duplicidades y fraudes electorales, ayudando a fortalecer a su vez la confianza de los ciudadanos en el sistemaAdicionalmente podemos integrar una confirmación de número telefónico o email con OTP (One Time Password de corta duración) lo que reforzaría la autenticación.**La nueva credencial del INE (2020)** ofrece una llave pública con este algoritmo en forma de QR que ofrece los 13 datos: CIC, ID Ciudadano (OCR), Nombre, Apellido Paterno, Apellido Materno, Entidad, Municipio, Sección, Vigencia, Fotografía con marca de agua, Modelo de CPV (nacional o entranjero), Imagen de la huella, Tipo de CPV, Firma Digital![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5wJg6l4DIFFmzjN-wFgaYQ8SOZVmPVhJ4ehYHT0IbQEE8VLkI8JMnj1t6sLxNL8yQBT_bo6sWc1BxUmNwVqzL_jy-TZCnk5J95vHDVydT1UmEcf4-u9DrWC9Jo96Jc-n5svypmfO78fVkbuldeq_GUfM?key=bmTiORLivl5REObwqZ86Hw) | Parámetros de acceso:1. QR Bidimensional encriptado (Llave pública en credencial para votar INE, posterior a 2020 con 13 datos) encriptado en RSA (llave pública / llave privada)2. Reconocimiento facial (Machine Learning, regresión de matriz gráfica a partir de referencia fotográfica del padrón del INE)3.Firma Digital(Machine Learning, regresión de matriz gráfica a partir de referencia cardinal y estilográfica del padrón del INE)4. OTP (One Time Password) para confirmación de email o teléfono (frase que expira en segundos para confirmar identidad)**Identidad** digital única en la blockchain. Esto permitiría asegurar que solo las personas autorizadas puedan participar en el proceso de votación evitando el adulteramiento del padrón **Inmutabilidad**, ya que cada voto registrado en la blockchain es inmutable y transparente, lo que dificulta la manipulación o alteración de los resultados de las elecciones. **Verificabilidad**, ya que cada voto registrado en la blockchain puede ser verificado por todos los participantes de la red, lo que brinda confianza en la precisión y validez de los resultados. **Auditabilidad** debido a la naturaleza inmutable del encadenamiento, es posible realizar auditorías exhaustivas de los votos registrados. Esto puede ayudar a garantizar la integridad del proceso electoral y proporcionar una mayor confianza en los resultados. |

3. **Transparencia** 

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Perspectiva electoral**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Infraestructura**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| La **confianza del voto** es fundamental. El código abierto permite que cualquiera pueda ver las entrañas del funcionamiento de la aplicación y para no evitar la analogía para recuento de votos, se propone la impresión de **boletas digitales (con rastro del encadenamiento y encriptación)** que se imprimen (ticket) de forma remota en la alcaldía o plaza municipal de tu comunidad, cómo se hace actualmente pero a mucho menor escala, ya que se llevarían a cabo bajo vigilancia, encapsulación y a la orden de observadores electorales. La boleta electrónica se integran datos no sensibles: CIC (ID ciudadano que es atómico en las bases de datos del INE) y el ID del candidato electo (del 0 al 5 dependiendo de candidatos en contienda) Al mismo tiempo quedaría rastro de ese código en la boleta digital que se almacena en el dispositivo móvil de igual manera encriptado | Ser **código fuente abierto**Posibilidad de compartir **resultados en tiempo real** en otra plataforma **sin comprometer la identidad del electorado**Minuto a minuto el voto encriptado resguarda la identidad del elector y aquí se propone mostrar en tiempo real los resultados (datos que se almacenan en paralelo con una base de datos NoSQL) con el timestamp (hora y minuto) y ID de candidato electo (valores del 0 al 7) En este caso usamos Charts de Mongo para mostrar los últimos votos en grupos, por minuto en intervalos de 10 minutos. ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcsqUSqqhKIScEsxW2xOKWkH6JQjWjUAxQpYhu1pE8mTstMcIgACZu9fuLl2A7ipuDileYrBCUHhGiDFUW8Gp1PYth0PmmvUHkKBU57xleuIbMrUuRz2KEPjwHJLVxjLb_RtY8e5Is6PE88muHm-0Mp9k0?key=bmTiORLivl5REObwqZ86Hw)[Tablero de resultados en Tiempo Real - MongoDB Charts](https://charts.mongodb.com/charts-project-0-wymtl/public/dashboards/655ba1e5-bf27-4f66-8452-5b12a58ebace) |

4. **Sustentabilidad**

| Perspectiva electoral                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Infraestructura                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Votaciones ecológicas que impactan de manera positiva a nuestro medio ambiente, eliminando el papel y ahorrando contaminación de traslados de electores, aumentando a su vez la privacidad del voto evitando el coyotaje, compra, extorsión, condicionamiento y acarreo de votosVotaciones más económicas gracias a la naturaleza digital y al necesitar menos recursos humanos, algunos persistentes como los observadores electorales, vigilancia civil policial y municipal | La logística de control de sistemas se reduce a un equipo de un organismo público en el cual puedan coexistir los observadores electorales y verificadores de código.Control de versiones al ser código abierto para ofrecer cada vez mejoras y eliminar brechas computacionales de ciberseguridad.La continua mejora del reconocimiento facial y posible vinculación con servicios de seguridad como el C5 de la Ciudad de México para la captura de autores de incidencias sociales es crucial para ofrecer a su vez un paso para diferenciar información pública a información sensible. |

5. **Ofrecer una nueva perspectiva del voto, el voto digital**

- [x] ![marcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAABbElEQVR4Ae3bsU4CYRDEcRsxodZE8Q0BbS258l5MwESJNL6HOfrPKdhyxeBcwk5mkn9F98sGIOSuPM/zPM/zPI+xG/SEtuiAWpEOaIOWaDIWziP6RK14OzSjX44ITvTBvqRn1MRaMIHeBIE2TKBBEGhgArWkKmtJBjKQgQxkIANd/Aw0NVC+O7RHvYFynHasN1COE/UGynGiXgOIjxOtdIH4OGJAfBwxID6OGBAfRwiIjyMARMCpCjRF5+72Dzhd5R+rHfpC92NeTlWgLl5PkQg4RYBynBSJgFMGKMNJkQg4lYFeUDuFRMCpBXQOEgGnDtA/kPg4xT7m2y/tCd9zKgOdviTC5RQEIiAFjh4QASlw9IAISIEjCURAWvmf1UDKcQwUSDmOgWLdMcxA7BnIQAYykIEM5EcRvplAW0GgNRNoKQg0ZwJN0E4I5x1dI+pmgSSA84BG2QQt0LrYG/eAXtGccjme53me53me9wPjPWZWjhktAQAAAABJRU5ErkJggg==)

  **Más seguro**

- [x] ![marcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAABbElEQVR4Ae3bsU4CYRDEcRsxodZE8Q0BbS258l5MwESJNL6HOfrPKdhyxeBcwk5mkn9F98sGIOSuPM/zPM/zPI+xG/SEtuiAWpEOaIOWaDIWziP6RK14OzSjX44ITvTBvqRn1MRaMIHeBIE2TKBBEGhgArWkKmtJBjKQgQxkIANd/Aw0NVC+O7RHvYFynHasN1COE/UGynGiXgOIjxOtdIH4OGJAfBwxID6OGBAfRwiIjyMARMCpCjRF5+72Dzhd5R+rHfpC92NeTlWgLl5PkQg4RYBynBSJgFMGKMNJkQg4lYFeUDuFRMCpBXQOEgGnDtA/kPg4xT7m2y/tCd9zKgOdviTC5RQEIiAFjh4QASlw9IAISIEjCURAWvmf1UDKcQwUSDmOgWLdMcxA7BnIQAYykIEM5EcRvplAW0GgNRNoKQg0ZwJN0E4I5x1dI+pmgSSA84BG2QQt0LrYG/eAXtGccjme53me53me9wPjPWZWjhktAQAAAABJRU5ErkJggg==)

  **Más confiable**

- [x] ![marcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAABbElEQVR4Ae3bsU4CYRDEcRsxodZE8Q0BbS258l5MwESJNL6HOfrPKdhyxeBcwk5mkn9F98sGIOSuPM/zPM/zPI+xG/SEtuiAWpEOaIOWaDIWziP6RK14OzSjX44ITvTBvqRn1MRaMIHeBIE2TKBBEGhgArWkKmtJBjKQgQxkIANd/Aw0NVC+O7RHvYFynHasN1COE/UGynGiXgOIjxOtdIH4OGJAfBwxID6OGBAfRwiIjyMARMCpCjRF5+72Dzhd5R+rHfpC92NeTlWgLl5PkQg4RYBynBSJgFMGKMNJkQg4lYFeUDuFRMCpBXQOEgGnDtA/kPg4xT7m2y/tCd9zKgOdviTC5RQEIiAFjh4QASlw9IAISIEjCURAWvmf1UDKcQwUSDmOgWLdMcxA7BnIQAYykIEM5EcRvplAW0GgNRNoKQg0ZwJN0E4I5x1dI+pmgSSA84BG2QQt0LrYG/eAXtGccjme53me53me9wPjPWZWjhktAQAAAABJRU5ErkJggg==)

  **Al alcance de tu mano (_smartphone o computadora_)**

**Siendo instrumento de una campaña de voto con sentido, participativo, de comunión y responsabilidad cívica (voto con intención)**\
\
Aprovechar la transparencia que ofrece el proceso que se propone desde la comodidad y secrecía de su hogar, y el sentido de responsabilidad cívica y social del entorno donde nos desarrollamos para lanzar una campaña de un voto con sentido, un voto con intención.

Un voto con intención podría estar vinculado al sentido de pertenencia del lugar donde nos desarrollamos. El Presupuesto Participativo como invitación a la mejora de las condiciones de seguridad y recreación del vecindario sería lo ideal para poder crear en la sociedad sentido al voto, no solo de elecciones sino de consultas ciudadanas. Que su participación repercuta en el presupuesto del estado de manera directa

Estas medidas no sólo fomentarán la participación ciudadana, sino que también promueven un sentido de pertenencia y compromiso social en nuestra comunidad, al reconocer y recompensar la responsabilidad de los ciudadanos en el proceso electoral

Un proceso electoral a través de una aplicación con resultados en tiempo real y autenticación biométrica ofrece transparencia, confianza, acceso y participación ciudadana, así como incentivar el derecho a ejercer el el voto. Estas ventajas contribuyen a fortalecer la democracia, garantizando elecciones más justas, seguras y representativas para todos los ciudadanos.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeFKi28FGG6H8EVU1Ah4s0KERpyuTj55wcPPiZC0YhRBRtDqlClgzqX7phqSljX6JNOKiyjsJX9h7jUunFVp0o7EL0RN409O9G2oIYokHZ37vnGtpz2pcg1O1IizSdn-zwjJ9ZXa_bhQQZun2vOK8VZyHTm?key=bmTiORLivl5REObwqZ86Hw)


#

# ¿Qué es el voto encriptado?

La criptografía de **clave pública** se basa en la intratabilidad de ciertos problemas matemáticos. Los primeros sistemas de clave pública basan su seguridad en la suposición de que es difícil **factorizar un número entero grande compuesto por dos o más factores primos grandes**. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdR4V5r2NjVo_l3fgcasbPrYJWjnKayZoWCS-t9GJK3a0_52MjELSpHX88lHbsbpUs020AqZ9z2laK6HNgiq4_RvwT4LUWkBA24ctfIh2UWso3iZS6TWwYcbRzGRNoSfst56AqJbp8HfFa5xQepmKvpEtY?key=bmTiORLivl5REObwqZ86Hw)

Para protocolos basados en curvas elípticas, la suposición básica es que _encontrar el logaritmo discreto de un elemento aleatorio de curva elíptica con respecto a un punto base conocido públicamente es computacionalmente inviable_: este es el "**problema de logaritmo discreto de curva elíptica**" (ECDLP). ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfhKcoeq0INORH3jmRuzgD5IMbCZ7_rKIqZqo9RaND6WYt-KiZN5ytSeCEWKHKzoyj6I0oroHne4z4_PtkC-hnXnR0LjpCR072twoVtjYhZtqMn0cbDnnUgWQR3Wzj4UJ199uGhY0D6DSnAUfVX2ZOyuBE?key=bmTiORLivl5REObwqZ86Hw)

La seguridad de la criptografía de curva elíptica depende de la capacidad de calcular una multiplicación de puntos y de la incapacidad de calcular el multiplicando dados los puntos original y producto. El tamaño de la curva elíptica, medido por el número total de pares de enteros discretos que satisfacen la ecuación de la curva, determina la dificultad del problema.

En una expresión algebraica tendríamos: 

**“Dado un punto (**[****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRwpMOixqkbtLhCHDlpi8zjbVMOqKzHiPn3OILZiBUnk7Lb0TUIpSQiMjabw97I07SHP7JnrIvKdvjk1t9seYANTIZa0pu6j9UuDSZVXEeLrFXMgj5vVp8Qbt4jcUWCdJ7EKpIcR6YNjrLCwkk09--wwmj?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=y%5E2#0)**) de la curva (**[****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeAOZPQ1SzKVOAqtqPRCr0u6n3ebgfRhFvSxycC6H-wl9ASqWRmchPSjtHUUCVtaeUmgV3aJykTgKA2hSLpwjKEmZX2YpjgoeJRiv77hFUrKTjuc5EGj36coPn3yECG7KaOkJmp3aIVt7lL6Uq7nNJMqLTw?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=x%5E3#0)**) obtenido del producto de un número entero:** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwFL6TOvpjLkhAFLhKhn2ySDZnCac1UEyIeKaO5PCNimWvvHQY1bQAeIZBJlJf78ovnhP252mO2dhHeIrwjc7dxd6Qrmy6E4KUw5VXNQVN2MepI0f6EvPiTo8DMJHk5K0oVlWYHxvvuINwSAZegYUlzZ4Q?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=Q#0) **(a) de un punto** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXT_YE3QgQhPnPrMzqP-1HxJiVQDupjxtdaAMWyDH5hB4Zgstrur8UBb5HMoKI1oU2CxEjbkPZoaNm8ZiQWKf6iYdMTAxcmyGQkSL2I6ffgxFhgOLbOPjZSyggbRx0a2v_5UrztPyR6JME6JJ3Z5aL_Zt7?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=n\(x\)%20%2B#0) ****[****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfedIJfDiKrlfNy3uYCiiM34q8qAyHVIE8rocE3UJ1aBGRjHb6kMPJgpJbS0uhcyWCBWGksNd-KFJyttq71GR3Cq_xTs9VKUVyGeUodVX07YDRo7PhV9WepJ1WTqX6xEACbBH1I4NYQZsXznIoIqWuqHpeJ?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=P#0) **(punto). Obtengamos el valor de** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7LEc7sCuFo2WgDciFITi6YFb3kI5VQ4v4To9F_GP5hs1eYIYki0zPbQOGBNMOsRw9q4lRB13_E66neq6bH8JHalXS-1zj_7pGAUWqdpya4n2P6oK-RYzzLpLw8dqqwYDDc4GD8Fnn_QwJPIRZSoV0ZNbk?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=n#0) **conociendo** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc2o6TY5OTYvgd6pKSmQTNBhvp0kYz7aDyqWexlIx8JxCD_xBDHHvj3R2cO7LwxDrds_K0oxNQWZIEDlsBnBw94eZ-1CpvQtioHfLouFj1o3N1c4GlmxGCNGkEWfel3nfTL38CXCdIipKdafURfyHiBew41?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=P#0) **y** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd6Yw9TCJwlDbCazdnc8fVt57ysvQZcCsFSYMV7T4DBKv-EjbUEe09fKx7jQZYgnQd0xxvSpH_iWubYXhN0xEVAP1sIrhuQi3bv9byqm2HZkB-P5-LkOM-6yVC8kw4f0gqCGUGbqKClrlvSqAHZsKv4GAYX?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=Q#0) **=** [****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfCVP1KoYhnix-4sNuj4x8PhMl8D-_wALqXB9KowYssywAbsRc905SZ4AttDtP2wp00656e_ZyXv_0-gcYAQITNTb31j9rCE7TiVM84ew88y5KP7HwkZ6ADl8fIF1xoHP7b_2zG53TO7ENCC5KaGqWHThoJ?key=bmTiORLivl5REObwqZ86Hw)****](https://www.codecogs.com/eqnedit.php?latex=n%20%5E%20P#0)**”**

[![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXftD6Gw-0tVtgRnlgfpkfhUrxbW-2kilaUZ28EDhZaS5CVhJ2qtx1PRmu6LD8BEXWQN5KTEs2rDMsNHeEsAwWDes2fLEXPoN0kGd4RlpnKFUhlOaMwV28G0ua9yp_U6_Hd6937HIIed0fifCHolb2r-Yks?key=bmTiORLivl5REObwqZ86Hw)](https://www.codecogs.com/eqnedit.php?latex=y%5E2%3Dx%5E3%2Bax%2Bb#0)

1. Durante el proceso de votación, el votante crea 2 pares de claves (llaves) ECC. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfHG43oS1SHMOVXaVie7Qk0LyS-p4LmGmo8yFcc9GagyC0YkRxcaZDYes_APncZ5vzflnC0ixmIUBQxvhtyTer2MsB5g0vcfbdDlIHehcyF6Lsl_qrrduBYr27zmOx-OAYtpWCEbfdq0IdkZMLCQ5nPdXA?key=bmTiORLivl5REObwqZ86Hw)

2. Con un par el votante revela su identidad a un verificador que certifica el primer par de llaves (claves) 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdvfMBSgDwwMRXuexVwn8F_7bRwDJ4m98yqx9eVOUTOvLI5y8kGfTJ9bgW2fZSSaFxF7yCJUVuDJ8xmmiAajQwZBOvQ4_1JI-puIrhnX0bdVPCRu1Duxa96Q90VaHjXXtgpxxZoGOONRwmvXe0CKpGfYpa3?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYGsianxji9dyV8j7G4b5eM0GR9oE-dPKbv1V5t0zYV-YpvBvZm207ccPmTuKxvf6iSl80XTQLlFrgyAkYxcbNNmO50ja-0M2h-FnP7e3sQ-F58MAK8usUxqE55YBYUPqr6sVTPP8gU7uTbN01U1Hbks9n?key=bmTiORLivl5REObwqZ86Hw)

3. Una vez hecho esto, el votante registra su segundo par de claves (llaves) de forma anónima que vinculan la pertenencia a su primer par de llaves

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeeKVr_VkkHUIgappxIRLtiHCMVqssl4jry_LZIRisJO-Bu4RU_1iZ7DfZngomfu4T_lB1usCG1ZO6AYo1dGNqydxaWuibuiEmSTw97knBYBxqOV7CyhhEZUjPLba2-TI32EpTZC4vjARZ1Hl3xy-vz2DLi?key=bmTiORLivl5REObwqZ86Hw)  

\


4. Luego el votante emite una boleta digital y se contabiliza en la votación con su par de llaves privadas.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3NJwNg_ALJAzGJZa-NMIdsql0-lL6YmMi_QMYQVuQPWgIKx1LZyg-D7Eq-KfQORi_aCRfDzPjxhxAvBSeuAvUPuN8sirKvZzqyAlv0IFPbAwHmenWyXsSrTrKhcxrblN-_yFFjCOqGlI-7qeh2jN-rwXW?key=bmTiORLivl5REObwqZ86Hw)  

Una vez finalizadas las votaciones, cualquiera puede verificar si la firma es válida o no y asegurar que ningún voto haya sido manipulado. Todos los votos se pueden verificar usando el par de llaves públicas para saber si provienen de un actor legítimo.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdTMILv6uRQqd5eUzI8fR_PQh5Iht-o3ZHaiL4Wjsk2HAJdJKvQi7RPb5HkA6LgZAR8XipWdMYKG_M6Uu0lkSUX2dRp_zK90raGajWnoELHw0wUjKAl3RHJvkDeE80n-KBGdxkqtTAwL20ClRK7DmW0ssg?key=bmTiORLivl5REObwqZ86Hw)

\


Imagina todo eso ahora desde la privacidad y comodidad de tu casa.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXflrIKSwV-mINnDxQ1qoIVsyxCJddM9KCUGNWG07c_vhWdFs8wUwTeANPU6hsFqacqLHCZXWwVqV3zQsk0UcVQOunTL2mzrpXTRtGPeK34oZA3VBqizEVLIeV6QtXzpM9-hjwIt6ACT9o5VWZceHobnOXkY?key=bmTiORLivl5REObwqZ86Hw)

Éste es el voto encriptado.


# ¿Cómo se encadena?

Cada voto tendrá una marca del voto anterior y el voto siguiente.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUyTUVavV0WqM-FNFsbK1TtdNZwo7lAXEltq3HtHFamRGjcwwEYvZoN4i3hKnbp9KNaUrKU9ee9D0kK76xA7bmEpqQlBciNmWsrcZh-UVWifVD8-uoz1QUksXd03wx7AdEu-G89hTAUdCPM9T9xxTz-sSB?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf9L52j4X7_7eISyboNMAQ167PF1H7BbL25hehd3-4Kn6KispbqGVCEyE67wK8Z5rIWg0YbNwMHHWHi2sWg4fxf2T0Oy4jeGME1MY-57egehvKbSzhTFs7nYyDLeYtUaFcwhOb1bxlqdEXEjZai7982mtkT?key=bmTiORLivl5REObwqZ86Hw)


# ¿Cómo es la boleta digital?

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcE4MbItNqE4tS9xGJSofULzEBavKxNTU5d2qODjH3bfep_vZEYYKgQcgV5paig7CN0hSfIzegmp1gIUFWD0YXq5KVgnmeqy2tuzaWZJ3rmVCxLpUwU7j-2B_2tLb-wsw2M3VgbWLF1x5Onsp-ft7DlbXb4?key=bmTiORLivl5REObwqZ86Hw)

Comprobante impreso: Acude a tu Casilla de Conteo más cercana y consulta la lista, compara tu código encriptado con el de los impresos finales.


#

# Ésta propuesta

**Demo de aplicación:** 

A partir de un escenario real que ofrece un voto electrónico íntegro, atómico, económico, práctico, encriptado, participativo e innovador con la premisa de _mejorar la seguridad y aproximar al 100% la integridad de los votos para evitar cualquier tipo de fraude o manipulación._

__![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf3TXD5OtGzVBOftm4xY77lsDo-2e5E-Wb4unbJaw1mCFHIgyf7ESGjT06d4o3JAoyW3zQmEKViLlem7hd4e7HRC4tD3sC7Wr60DaX9VDZjsXcqgi_dIB8-R-PVc6mBjH5bdNILF2j9a_ACLauqBNSy8zs?key=bmTiORLivl5REObwqZ86Hw)__

**Código abierto**: 

Lo compartimos en el repositorio de código más grande del mundo, lugar donde también reside el código de _bitcoin_, me refiero a **GitHub**, la comunidad más grande de desarrolladores y fanáticos de la innovación. Conforme al código abierto que se enfoca y refiere a los **beneficios técnicos** que se puedan adquirir al compartirlo.

Acceso al proyecto público:\
[**adanqz/Demo\_PP\_4\_URC: Demo de votaciones vía blockchain (github.com)**](https://github.com/adanqz/Demo_PP_4_URC)

**Baúl temporal:**(_Posible fórmula de un padrón veraz y transparente_)

La estructura de la base de datos no comprometería jamás la integridad del elector en este caso específico. Los datos sensibles se encriptan. En la práctica el voto se envía a una **base de datos temporal** donde se aloja solo el timestamp y el folio encriptado de referencia.

En este proyecto se estructura una base de datos con JSON, el cual integramos y ejecutamos consultas en Python en complemento con la librería PyMongo.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXejWyPWCHjTW-81Ygz1wx-LCLhIC6QMPCPBl0lWjs48rBDhZ4ztUimnsRBOVP0867u-au5X9-giUP8wiN5gPecNNfCwr1OXs3sdcer6yvdWa1S8gQWe3KIR_MZWanUT7PYlD_8CM1zQ1aX15nFbHqhm0pCM?key=bmTiORLivl5REObwqZ86Hw)\
\[Ejemplo de la estructura del padrón generado para este proyecto en particular. Alojado en Mongo Atlas. Base de datos NoSQL (JSON en este caso)] Tomando como referencia los 13 datos que ya incluye como llave pública la credencial de elector de 2020 para adelante.

En la práctica, lo ideal sería emplear un conjunto de combinación de base de datos **SQL** y **NoSQL** _AKA_ **persistencia políglota** para poder dar abasto a la cuota de carga de la plataforma y al mismo tiempo evitar el desgaste de recursos a nivel de hardware y memoria virtual por ejemplo AWS o Microsoft Azure lo que permite interconexión de envío de datos a través de una base de datos o más simultáneamente y de manera descentralizada y con la infraestructura necesaria para los efectos de los algoritmos de aprendizaje de máquina (inteligencia artificial).

**Topología de red P2P:**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiPeKco_DjdEDtQQMLKDhZ22w6pbIKiZ9ffNtC0IQmgvfzCxW4yiiShCA_UhRGQBvRlZy-PhCxL3L00jfkDf-0KsJnqx7RhkFbzaaWFaaYJtADwVSTVMLdiEmmDavsVWBZvOJny2SE3JWQShzEalY1HQqt?key=bmTiORLivl5REObwqZ86Hw)

**Cálculo de rentabilidad:**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeovt8albWPObs3Uj0IVA0p17IvMVid3UAtOoAHEi5GoSs7oNNea-KrurFuflCpnrEQbBjrGDh6hyrGYuGjWGnZuDx_RpXHE9X_zjMFcyn7L6kjs2Hd6mkpUnrjg2JhKCZhCXSWQ0cUh_qT93zaUqvDBHJI?key=bmTiORLivl5REObwqZ86Hw)

Un plan financiero que destacaría los detalles en cifras para poder darle mantenimiento y soporte a un sistema como el presentado. 

- [ ] ![desmarcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

  Elementos Humanos (OLDs y OCDs observadores de larga duración y observadores de corta duración) / Tecnológicos y Financieros

- [ ] ![desmarcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

  Autotransporte habilitado con impresoras de boletas digitales y vigilancia en tiempo real (cámara de vigilancia)

- [ ] ![desmarcada](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

  Conexión Wi-Fi (Conexión compartida desde dispositivo móvil)

**Predicción de participación (Comicios del 2024):**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXetqHYAByNiUrOwrMxwAcm-sWXguxnMaDf3KpnXo96dLQRc8ZLz9GVOyzdhV0Aw_1nVV7NHQv-XDncVknDWwArpmBrR6V-YiV0LJfzGNfptlF8ve9EomILNtyJSZeTtMjPss8gTHq-8yTeeit6lDn7DjFDQYrCnO1oUQxTO?key=bmTiORLivl5REObwqZ86Hw)

Gráfica de calor que muestra el porcentaje de la participación ciudadana \[**ATLAS SICEEF INE 1991-2015**]

Los datos históricos de las elecciones presidenciales de diferentes años obtenidos a través del **ATLAS SICEEF INE**, incluyendo los porcentajes de participación ciudadana total en cada elección son en efecto, un _dataframe_ para generar un análisis de regresión.

|          |                                            |             |                   |                |                |                |
| -------- | ------------------------------------------ | ----------- | ----------------- | -------------- | -------------- | -------------- |
| **Año**  | **Elección**                               | **Nominal** | **Participación** | **Porcentaje** | **Abstención** | **Abstención** |
|          |                                            |             |                   |                |                |                |
| 1994     | Presidente                                 | 45,729,057  | 35,285,291        | 77.16%         | 10,443,766     | 22.84%         |
|          |                                            |             |                   |                |                |                |
| 2000     | Presidente                                 | 58,782,737  | 37,601,618        | 63.97%         | 21,181,119     | 36.03%         |
|          |                                            |             |                   |                |                |                |
| 2006     | Presidente                                 | 71,374,373  | 41,791,322        | 58.55%         | 29,583,051     | 41.45%         |
|          |                                            |             |                   |                |                |                |
| 2012     | Presidente                                 | 79,492,286  | 50,143,616        | 63.08%         | 29,348,670     | 36.92%         |
| 2015     | Diputados RP más Candidatos Independientes | 83,536,377  | 39,864,082        | 47.72%         | 43,672,295     | 52.28%         |
| 2018     | Diputados RP más Candidatos Independientes | 89,134,077  | 50,143,616        | 56.23%         | 38,990,461     | 43,77%         |

Calcularemos la media aritmética:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZlzbKCj5hGkw1_15F5daaFHztlefQndIvjxzHsg4VToQJ0XlSaBKtzGKtz9duwsRFmpRR6exr1bHUS1ZIcf2rsk7aK3hu5askQlFhROZK_ADr5dcZmbN562vV6UENMOwl33Sh3WDBuRhSEKkp9-9LiHCD?key=bmTiORLivl5REObwqZ86Hw) 

Media de los electores: 41110260.166666664 ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdD2fxdOApH1I-FFgERdZdjgwP0UcyO0Ce-5_bvbeTOXnAUGh3365vdGrIP8nUIjkv1bd42MjEF5zNq8Vj-nvlH6fKAgo0y_XAtQaFPNchzljGvBucdI998AUcn-LdORPILytw1nLlH7eSlP6k66EhXAX9A?key=bmTiORLivl5REObwqZ86Hw)

Varianza de los electores: 21768004485295.473 

Desviación Estándar de los electores: 4665619.410678015 

Media de la población: 71341501.16666667 

Varianza de la población: 224241434847265.5 

Desviación Estándar de la población: 14974693.14701525

Xi<sup>2</sup>: 6.327316670945114 

Valor P: 0.0422708170418046

Vamos a calcular la tasa de crecimiento promedio entre cada par de elecciones y luego utilizarla para proyectar el número de electores en 2024. 

Tasa de crecimiento promedio entre 1994 y 2000\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3KlRS6AGoYuXW38VDt5w4t8zWIR946NvdEKrG3WGKhgK3X02jiRYo-u2YHHSWReBT8VER1Mu0foduESMAlzwp4zyrVlnyiY_JixVpC8aQrzMV0ODiQ8dBAKPxtpgW45RF_ygv4x_JJz0VuY5oL9aKhy26?key=bmTiORLivl5REObwqZ86Hw)

Tasa de crecimiento promedio entre 2000 y 2006:\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWsZ775ri00TyJI-z8tfhubGAOdYR0X0WX94i8sMG6knju9xeJdtFq9vUw-2Y1mZqswX5TMJ-UyVqxIINw8qWAhHbxOAkwcBi5kKSBT0DAw4DV3tnpCoo8WDzz_bdNzWdCYnUIqAJXLw8uDbXtdUk37r_d?key=bmTiORLivl5REObwqZ86Hw)

Tasa de crecimiento promedio entre 2006 y 2012:\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeCnMpejtTczO6nOnxmeA4EQvx5GtYsxkMd_bRsw1tyIBzzfMFMH7cuKkSL1D49IWqLNOq_Y7i5az_jPJidO7thDS8xkXk33rhtmOakS0RXcyTmjIIgVjjBvzWel_krgUOfnBzyVraO49UvzP5fQnomSOXS?key=bmTiORLivl5REObwqZ86Hw)

Tasa de crecimiento promedio entre 2012 y 2015:\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQkgD7AXEgzoAgC5uMzaNMevHeJM4IV0Y5TE0ZOnwkFeCEksMVvZe58hvOAwvseX1BYsgO933Tmn4daASsmbttJvPQCorViqdtkqmAs3YYZDBa8y_jPXB4z6nX1mgGh6zUKxxbvkeBg0W7SOtZ?key=bmTiORLivl5REObwqZ86Hw)

Tasa de crecimiento promedio ponderada: 0.1510

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVu1-hfVpsn3yHOvB04e3qFhcUPYTlMIkf9SX2_is8G21v_AuHu9CKJKC7saLvLb9lBBO3I-XpqUh3X_pZZUjpWmL3uOYV2EZhYN2puLYzBXvZftXeEWNuP18i1zFcDq6GBA6HNL7iEkTEIzPlvHJZbOs?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNQTWfpeDd_pjefoAY4010d86CeWhX7jSMI_CUNUJEZJoydsyVdje2cE1xykH6jUiEb3UO4M17lXsf4EYe7z5L2ZwQuB6IOuUuqSXn5RPD5EWnoGW2LzdVG7LwAY4TH57tbS04oVSfAP7lXvX5anNHOEQJ?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeTAKbWDyzVDLWZZvmeHXx75LmdDMWdn5iCQoFWXpTXE5wePR6zIF4CN_F6iXsHBV-kPwHpsDUbGvXxYk_GDuM__iIeCOn2wpbZMbihHEYILqx11V31oCxGJTNNgTjYtfrxJP3mzA56-21raGaU41CwY7kM?key=bmTiORLivl5REObwqZ86Hw)

Número de electores en 2024:\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcuv83tpjNoLfS-F7cE_TnqLuIT8JvGFndq7fpo3w9RUJBQ6ogQzWfB1KpDNbyRv5t3waeRg7LXY4TQ-CVwJpQdPu18XLfoPeZWdg0JVv_0TmpWjpL9MEj6ia33mHXypUyKmSHuBuCQkDHDCXk99EElZcs8?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfstC5RP7bZe0VXaXpaS6wIs4k5U5idYl1uRuTamc4t5cs2IIc2sO4ioptj54ypxJ4B1wtvFlkmH1KEsMAf_pTIWQRTHZS6yYY4q1F7Kq3mGWOgS4CZUiDJtcTK9-pV79PLJgbgsfzWlDYu7KxchfFuRRyk?key=bmTiORLivl5REObwqZ86Hw)

Por lo tanto, según esta proyección basada en la regresión lineal, se estima que el número de electores en las elecciones presidenciales de 2024 será de +**43,543,726 cuarenta y tres millones quinientos cuarenta y tres mil setecientos veintiséis electores**

Para graficar la distribución normal con la probabilidad de que las votaciones varíen un millón o dos, podemos utilizar los datos proporcionados y calcular la media y la desviación estándar de esos valores. Luego, podemos utilizar la función de densidad de probabilidad de la distribución normal para graficar la curva.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfdouHVxaoi7a7w3W4hCigfwzUWI9cYpQBbzGba_fSgAOacV3BPyFXluXuoPUKP27LvOU8xxpJEhSADVfPxCeSrr6tZSNBmR1yQBahdXwGTo0XfFT_13yiB4B457jgUp-lG_LI4lIec6jFvpSSLRdE4inE?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfX8pQmqWfaEXrXOaRe8dnhAbKXan90Ta-tWoeOVALhwnqGsEHkRlNSkRl4FAPYwchUwjCxrDrasXjRTPKTAk_lUYULnapQb2tAhey0BQdktxvttQZaPwjz-4W1AQRrLrUQbhu6d0cUOb3mPQ-WEiTHNLS3?key=bmTiORLivl5REObwqZ86Hw)

Hay una variedad de factores que pueden influir en los resultados, como datos demográficos, socioeconómicos y políticos. La estadística multivariada permite analizar y modelar conjuntamente múltiples variables interrelacionadas, lo que brinda una comprensión más completa de los patrones y tendencias que afectan los resultados electorales. Así como detectar relaciones complejas entre variables. Podemos identificar interacciones NO lineales que podrían no ser evidentes mediante métodos univariados.


# Capturas App ParticipoMX

1\. Portada:

__![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-6GKpoHwwa6t5Eq9XSVMEzrLhpRzxM0lOnEFF64e8Mh7ll15ojrzxHBZN-qBFz2AM_vwyhIo2XmAm_DsY5Z4M0_96cw7uORL-PbzA7vnB5ETfbTnN0Jv_N98AUtVi-r4QjtHQwahEVS65v_PL40oif-pp?key=bmTiORLivl5REObwqZ86Hw)__

2\. Identificación con QR y confirmación de datos:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe9ljEtrxRIxTUpavE-qdzilu463pyHVD9vPQtw6DnhihfUdYlxMUIqTuDHmXM6KV7DPd_z3SZV0pTiMSsFbQL1x_cuGxhEVjr_cwnBcYOyV57QpjWzHxmK3H54WgO1JdCD8rDByj-wptatZrOXiurYhmaN?key=bmTiORLivl5REObwqZ86Hw)

3\. Selección de candidato y confirmación

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeNNirxJ2osGki7syRrHOstHKG2BIymMkdByyovJJNBJMUw-X0-xa3VDTL2nGcP1JJYqXZzHh31qhvNW_dFUqIMOBx6FwKVoxCOpisrd6ojihgFg0HNw9-eRnR6ZwFcCC_h56x1y9cE2ijVLlO3CzMDG0U?key=bmTiORLivl5REObwqZ86Hw)

Llave encriptada en dispositivo, agradecimiento y conteo para Presupuesto Participativo de su comunidad (impresión de boleta electrónica remota de manera anónima)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfe7OdQbJg8KLlFP3gIDJJbV6eXV2jcosdZrYpE_7jLe0jT3Jynq9fg7OFJEwIOH2GSeZ712UjYpYPvSCGkQhMmVnSXIxxQWWmaO05tBi0DawQBG-NW5PCld6xCuVX0yfgJrCoM9JU001Py5SYjpG3CALMR?key=bmTiORLivl5REObwqZ86Hw)

\
\
\
\
\


Boleta Digital:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcE4MbItNqE4tS9xGJSofULzEBavKxNTU5d2qODjH3bfep_vZEYYKgQcgV5paig7CN0hSfIzegmp1gIUFWD0YXq5KVgnmeqy2tuzaWZJ3rmVCxLpUwU7j-2B_2tLb-wsw2M3VgbWLF1x5Onsp-ft7DlbXb4?key=bmTiORLivl5REObwqZ86Hw)

Urna Electoral demo:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKLZpbpTo3YcG66_WkC4-_BJbieOMpdDE6dcXa67ORU7sX_kcZL5wq9FkjUBUA9LqPAZVPpKIOImzOZlE02ZGaUrOfNsX2eChT9TdRiueaeyb_xu6toAPpW7WjsGV1Z2E1Pk-iFvN9SLdfKlKWxkXqbc89?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4oPJubbXWSvsS5tXl3T6Xrw-ZEu6GSxoZYrD_VxqagBMYHp6VzloUzFLh35tmhpV0BlQjdzT0Moq0ZZukJY8ahRLnYP3GR7uRMs-_D3iueQrJ9LYa7f76oLudJyXmiK4OeLnj71DF81sqFleMSf_26AV2?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe1vtglhTgRyxa3spjWngbanIjfXPcSHcD0M_JqwmFpgt4XJwjmVo0V24iP7dIrAr1UZstaLjztPcfU6bUtPdl018i4nCQeASZZifxanEHw0jG4oUofN2FiK-JnN5_ZiF18-pPrddRNHE9q_JqzDk_MQxY?key=bmTiORLivl5REObwqZ86Hw)![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdP0H8otV78eJtbYzWh02ZnZNoeP2vdS4HEwiZlJ2VIwrZXOleMWJLt3_Rf8ldiSZ8QIIcdB0Gn-9EHXAMwDqNsm4YAzVxWnsEAVXLzACjyWJF3cgSvHIvDFZsuSkrvZfEa18KevIbB04SjCYiKdgrph1sG?key=bmTiORLivl5REObwqZ86Hw)![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXczGv5lo6hBHI_lrDMcGmbkBD6oABjUD9HGH7d65I_ZsLP5GXD6nPsmzQdhJeVZLSVdo3Mf6QYs4uFHhLxIi4P51cLh1m5QrBprxMoXo-CkC-lVIfRQu_kIx0c-sXMlzRKT8zHYHrMQLAB0H4FAnY863j2B?key=bmTiORLivl5REObwqZ86Hw)


# Impresión del voto

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXewXSJS1t93jhQDgxj7KxqadLASF_k5C2D6GwAwDpN0QglCddaReae5sPJ1RKU-mF_yvuiEx76J7iQwi9NgxqDHu9NLyH_8nbLe6QpE06Rer9unF3g8Jmf7MI0Uf6Vab4GF6jVO16Cb12IO_Z2rHceNNprr?key=bmTiORLivl5REObwqZ86Hw)\
Caja de encapsulamiento de ticket de votos impresos en tiempo real por casilla

Prototipo de Impresora de votos (encapsulamiento de prueba tangible para el conteo al final de la jornada)

La misma urna será vigilada durante todo el proceso y los OLDs OCDs estarán presentes.

El tamaño y función podría llevarla a las zonas más difíciles.

**Hardware:**

Pantalla a color![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd0bFkuoavqLoiku-Sbgh0LJ_nxOVg3Hl0SB_vq_PMAngk95NAYH1cyH092xnPHSXzuEZUKUwWPla4MRJAf-oADJoVfo-HLifUeJCMYZEVKZth4AinnbJYUZrRsrGS_hEPre975PFmpF18g5JBC7v7V7fY?key=bmTiORLivl5REObwqZ86Hw)

Impresora térmica![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf2sTa3Wcmu8VR2lME3KsXdonvKtU-j36VCvnRnWfY11RAKt9_R6d6rLe7WSS5h52ViD0C50yJP6mfqUhbeiYXG3O08lakgyLFFeKt_-WNH-a3cd698T_o9G45y1P3Un9VjZS-d9DWtczFbxYVDR450Wq4?key=bmTiORLivl5REObwqZ86Hw)

UPS ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2Sm7sS59MjKQZTjldrYUHSgNg8DHsQJPgnVtZqZSwny3xsbfDilq2OiozJxAy9mRN1v2TxCTCJYSopWKiMOIfk1z938ZqFIXGyukiHNJP2Ns97Kcgz68tfTFuRv4noRnytNuWxtqMOuAds9EH3hbOa0CQ?key=bmTiORLivl5REObwqZ86Hw)


#

# Encriptación del voto

Para mantener la secrecía del voto y poder mostrarlo en una tabulación o timeline encriptamos el conjunto de datos públicos y privados para poder crear una cadena SHA256 y enviar el dato público al tabulador y mostrarlo en tiempo real.

Para entender un poco usaremos como ejemplo la encriptación JWT (JSON Web Token) el cual tiene la siguiente estructura:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc4QXDEPSkMIZa8tQtbU0jV7CddFyMncbUBdewXrsrUGq4CC0eIpHahuYiCPWluarTX3KSYmBeJG_h9O8bmHiThKU8uY62tPggMYjiywD4na-Fm1QwfMxKgR0Owovp7FwLLE1nxyweXTL7qBxAEzofoXGG6?key=bmTiORLivl5REObwqZ86Hw)

En color azul tenemos la **parte privada** (donde viene la clave de elector y el o los votos encriptados) ****de nuestro voto que se compone de la encriptación del cabezal (que dicta el algoritmo en el que se encriptar y el tipo de encriptamiento) + los datos **encriptados públicos** (ID Ciudadano, entidad, municipio, sección y firma digital) que vienen en color rosa.

La posibilidad de utilizar **código abierto** (open source así como lo es _bitcoin_)   facilita la comprobación del código por el equipo de ciberseguridad, lo cual mejoraría la verificación del sistema en general. Esto está siendo planteado por diversos países, evitando así el efecto **“caja negra”** con el que las empresas entregan las urnas electrónicas.

El voto encriptado como hash final será una combinación del hash actual (voto actual + hash previo + hash contiguo) dando una cadena compleja y encriptada con marcas del voto previo y el voto siguiente y así mantener la integridad de la serialización inviolable del sistema encriptado.


# Tablero de votos en tiempo real

Creado en Charts de MongoDB (Acceso público)

<https://charts.mongodb.com/charts-project-0-wymtl/public/dashboards/655ba1e5-bf27-4f66-8452-5b12a58ebace> \
\
Podría usarse el dominio **ParticipoMX.gob.mx/votaciones-en-tiempo-real** en la práctica, este mismo será el que aloja el baúl temporal (red P2P)&#x20;

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcF71o_fwD2EblHY_IihLUOiBLT4aoxBnMh2IXORm6GOJM_c_h3pIRqFatcxA4TSHQdjtF-7nRZBHL50Jxu24GDHlkqCIHS8gA4N9JYS7gEpCGmCONGb8oxRt1C-n7c0IIvk4ex9Yb4TFnX4OSXRxlguJQ3?key=bmTiORLivl5REObwqZ86Hw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcsqUSqqhKIScEsxW2xOKWkH6JQjWjUAxQpYhu1pE8mTstMcIgACZu9fuLl2A7ipuDileYrBCUHhGiDFUW8Gp1PYth0PmmvUHkKBU57xleuIbMrUuRz2KEPjwHJLVxjLb_RtY8e5Is6PE88muHm-0Mp9k0?key=bmTiORLivl5REObwqZ86Hw)\
Dashboard de votos en tiempo real. Minuto a Minuto\
(10 grupos en un intervalo de 10 minutos)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdhqRAeymmP1G5XnQeJoopYD3ftRwAx2fBxeqgFiMzsEYc9627jUjiOty3jY9HRgeIZoZsiKBEdJqhLQhzDU0ZeP4DVXrdUhu5daE36mkT7jc0GUc0Od63s5zAWgjAqq2MmcnEywSSu5eQi9gGT36lJyIow?key=bmTiORLivl5REObwqZ86Hw)\
\[Imagen del rendimiento de cada consulta a la base de datos en Mongo. 17 milisegundos para examinar un total de 143,239 registros]

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcGuvkDOQGh900QeXVaOW2yMEhkCcJeGy9UhzTeYwz3tmzo11trJF8JGS-wnuGa1xbSNtpArDauyf-F9DzVczL3hNnVYHDCRbkzISUVXPyK36ZiafareybrQNmElAIhocvKMXoh9iv5C4sMOW8Tal4gjxqW?key=bmTiORLivl5REObwqZ86Hw)

En esta imagen se aprecia el cero, indicativo de que este registro aún no ha ejercido su voto o lo anuló seleccionando “Ninguno”.


# Diagrama de App ParticipoMX![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfyW2e5yEnf9tdglydKfObDYc-r374gYAAgkfGkjbh50bZ_fiTZfZFNMbj41z8zzAUnKEuA-fFLQb1IrP9WWDfKGNO8Ce6ETURpXSFQ1fl2xNKlbbgyLWqxT_-W6MFsyFxeBRTZW5UfSBf-0zARFp8nMubY?key=bmTiORLivl5REObwqZ86Hw)

_Padrón electoral\
(144 mil registros emulados con Python / JSON):_ 

\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeO-TYe8kkxNYOq3bhXLQb_0jg8HXbKcwjy_unMHoZcfO9yXIfk_25ykD0skZhOZtVztFYFWdSNb_hj6aoV2vRcBdXHwIYiwut_drrDIsEv2ud7h49H_05o3qqcXJVL90vt81Ljt3kT1Z8HE5cFIEubm1Q?key=bmTiORLivl5REObwqZ86Hw)\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfEMilyExNXzGAZCRlaDxnOjTkJThoKtW38yr_gbPkHwOkQFDaDJ9lWn_nUjGeoTtMqGVHTVnDX1Vu4TyZL_FIvwS_VmwMN9nahFF2CMj7I18rXBCce6BVC13M3uuNPm0meOxlLIQju_uNe9VPHDURB6_lI?key=bmTiORLivl5REObwqZ86Hw)


### **Mirar todo el código:**  [colab.research.google.com/drive/1rZEHpbb3hiS7Ak9nknhU3fjpi5T3s4oY?usp=sharing](https://colab.research.google.com/drive/1rZEHpbb3hiS7Ak9nknhU3fjpi5T3s4oY?usp=sharing) 

Un total de 143,239 registros generados

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeJ0-aF66EdSbcqMGIVhRLVwqdn8GVJr0BhUgVCv_D_wm1FqcjC46sii-t5FGDjtQ6HgN3Q6_Ue2TFcJLhcXkIsoeoxQkcmX4yW8s0X3MiU7psDyiOb0GJ2Ct9ZCIc_3s-_3X3p_yJAPt4OOBFNzEbVkX01?key=bmTiORLivl5REObwqZ86Hw)

Estructura de cada registro formato JSON:


# ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXejWyPWCHjTW-81Ygz1wx-LCLhIC6QMPCPBl0lWjs48rBDhZ4ztUimnsRBOVP0867u-au5X9-giUP8wiN5gPecNNfCwr1OXs3sdcer6yvdWa1S8gQWe3KIR_MZWanUT7PYlD_8CM1zQ1aX15nFbHqhm0pCM?key=bmTiORLivl5REObwqZ86Hw)

#

# Conclusión

Las tarjetas actualizadas del INE incluyen un código QR bidimensional con 14 datos encriptados para  identificar al elector (llave pública encriptada en RSA), garantizar la identidad del que ejercerá el voto en combinación con el reconocimiento facial y la encriptación con algoritmos computacionalmente imposibles de descifrar son un factores actuales que se pueden aprovechar.

Cabe aclarar que el voto electrónico es un medio más y, por tanto, opcional. En las primeras fases del paso al voto electrónico conviene mantener la presencia del voto tradicional. Comenzar con comunidades especialmente afectadas por la dificultad de traslado y así evidenciar los beneficios de un sistema digital. 

Dar entrenamiento a usuarios y gestores. Ir paso a paso analizando las fortalezas y debilidades del sistema para mejorarlo cada vez más y poder estandarizar. 

Asimismo,  es  muy recomendable  poner  en  marcha  reuniones,  foros,  mesas de trabajo, _hackatones_, entre estados y naciones con objeto de intercambiar información y experiencias que ayuden en el desarrollo y fortalecimiento del voto electrónico. 

Todo desarrollo en esta materia debe de ser considerado en el contexto que está situado ya que las variables son amplias, y al tener presentes las cuatro dimensiones que la rigen: legal, política, social y tecnológica. 

También hay que considerar desde el comienzo el tamaño del proyecto que se pretende implementar.Es necesario desarrollar un esfuerzo importante por partes de los investigadores, apoyados sobre todo por sus mandatarios, en pro de realizar estudios que fortalezcan las bases de una democracia.   

Intentar convencer a la gente de que el _blockchain_ y las impresoras en las entidades electorales son seguras, no es la mejor forma de introducir el voto electrónico. Es preferible hacer todo el proceso **transparente** desde el comienzo y asegurarse de capacitar adecuadamente a los observadores electorales para que sea un recuento con resultados fiables, rápidos, claros y verificables. 

Utilizar el **código fuente abierto** en los desarrollos para mantenerlos **transparentes** y así facilitar las auditorías, pruebas de seguridad y certificaciones para estandarizar un nivel de seguridad aceptable. Se aconseja enormemente dejar atrás el empleo de equipos con estructura de “caja negra” ya que actualmente son inviables.

En  este tema  se  producen  cambios  de  opinión  de  forma  continua,  lo  que demuestra que no ha sido introducido correctamente. En muchos países no se han resuelto algunos de los aspectos del voto electrónico (legal, tecnológico, social, político) debido a que no se han explicado claramente las ventajas y el interés público es casi nulo. Los mejores  desarrollos se  han obtenido  gracias a  una  estrecha  colaboración y  entendimiento mutuo entre los expertos  tecnológicos y los jurídicos, para posteriormente incluir a los legisladores, políticos y público en general.

No olvidemos, finalmente, que todo es cuestión de confianza, la gente cada vez compra más en Amazon, Mercado Libre y se beneficia del ahorro de tiempo y dinero en traslados. Sin dejar atrás el uso de Apps bancarias que va en aumento exponencial. 

¿Es el momento perfecto para comenzar a conocer a investigar la curva de aprendizaje de las votaciones electrónicas en México? Tal vez en las elecciones de 2030, sí.


# Bibliografía

_ABC Electoral - No todas las credenciales votan (N.d.). Ine.Mx. Retrieved November 6, 2023, from_ 

[_https://www.ine.mx/wp-content/uploads/2022/10/DERFEABCCREDENCIAL2022.pdf_](https://www.ine.mx/wp-content/uploads/2022/10/DERFEABCCREDENCIAL2022.pdf) __

_Instituto Nacional Electoral. (n.d.). Ine.mx. Retrieved September 28, 2023, from_ [_https://portalanterior.ine.mx/archivos3/portal/historico/contenido/Estudios\_encuestas\_e\_investigaciones/_](https://portalanterior.ine.mx/archivos3/portal/historico/contenido/Estudios_encuestas_e_investigaciones/) __

_(2009). Ine.Mx._ [_https://www.ine.mx/wp-content/uploads/2018/01/DECEYEC\_Comparativo\_VF.pdf_](https://www.ine.mx/wp-content/uploads/2018/01/DECEYEC_Comparativo_VF.pdf) __

_Las, A., & De, E. (n.d.). "CULTURA POLÍTICA Y PARTICIPACIÓN ELECTORAL: DIAGNÓSTICO DE LA CULTURA DEMOCRÁTICA EN MÉXICO DE CARA. Ine.Mx. Retrieved September 28, 2023, from_ [_https://portalanterior.ine.mx/documentos/DECEYEC/diagnostico\_cultura.pdf_](https://portalanterior.ine.mx/documentos/DECEYEC/diagnostico_cultura.pdf)  __

_(n.d.). SICEEF 2015 - participación ciudadana. Ine.Mx. Retrieved September 28, 2023, from_ [_http://siceef.ine.mx/campc.html?p%C3%A1gina=1_](http://siceef.ine.mx/campc.html?p%C3%A1gina=1) __

_El Nacional. (2019, March 11). El caso de éxito del voto electrónico en Estonia. ¿Podrá replicarse en Catalunya? ElNacional.cat._ [_https://www.elnacional.cat/es/tecnologia/voto-electronico-estonia-catalunya\_363339\_102.html_](https://www.elnacional.cat/es/tecnologia/voto-electronico-estonia-catalunya_363339_102.html) __

_Beneficios del voto electrónico para la ciudadanía residente en el extranjero. (2019, October 4). Central Electoral._ [_https://centralelectoral.ine.mx/2019/10/04/beneficios-del-voto-electronico-ciudadania-residente-extranjero/_](https://centralelectoral.ine.mx/2019/10/04/beneficios-del-voto-electronico-ciudadania-residente-extranjero/) __

_Urna Electrónica. (2021, February 13). Instituto Nacional Electoral._ [_https://portal.ine.mx/voto-y-elecciones/urna-electronica/_](https://portal.ine.mx/voto-y-elecciones/urna-electronica/) __

_de Recursos Financieros, D. E. de A. D. (n.d.). Clasificador por Objeto y Tipo de Gasto para el. Ine.Mx. Retrieved October 3, 2023, from_ [_https://ine.mx/wp-content/uploads/2017/08/JGEor201707-12-ap-6-1-a1.pdf_](https://ine.mx/wp-content/uploads/2017/08/JGEor201707-12-ap-6-1-a1.pdf) __

_Modifica INE presupuesto 2022 derivado de las reducciones efectuadas por la Cámara de Diputados. (2021, December 11). Central Electoral._ [_https://centralelectoral.ine.mx/2021/12/10/modifica-ine-presupuesto-2022-derivado-de-las-reducciones-efectuadas-por-la-camara-de-diputados/_](https://centralelectoral.ine.mx/2021/12/10/modifica-ine-presupuesto-2022-derivado-de-las-reducciones-efectuadas-por-la-camara-de-diputados/) __

_Aspectos tecnológicos del voto electrónico (December 2007 Oficina Nacional de Procesos Electorales (ONPE) Perú Editor ONPEISBN: 978-9972-695-33-9 Authors: Panizo Alonso Luis Panizo Alonso Universidad de León_ [_https://www.researchgate.net/publication/259668840\_Aspectos\_tecnologicos\_del\_voto\_electronico_](https://www.researchgate.net/publication/259668840_Aspectos_tecnologicos_del_voto_electronico) __

_(N.d.-b). Researchgate.net. Retrieved November 6, 2023, from_ [_https://www.researchgate.net/publication/321803764\_THE\_FUTURE\_OF\_E-VOTING_](https://www.researchgate.net/publication/321803764_THE_FUTURE_OF_E-VOTING) __

_En, A., De Estudios, S., Europeo, D. P., & Boucher, P. (s/f). Cómo puede cambiar nuestra vida la tecnología de la cadena de bloques. Europa.eu. Recuperado el 21 de noviembre de 2023, de_ [_https://www.europarl.europa.eu/RegData/etudes/IDAN/2017/581948/EPRS\_IDA(2017)581948\_ES.pdf_](https://www.europarl.europa.eu/RegData/etudes/IDAN/2017/581948/EPRS_IDA\(2017\)581948_ES.pdf) __
