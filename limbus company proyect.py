print("""
    _            _           _                           
   | |          | |         | |                          
   | |     ___  | |__   ___ | |_   ___   _ __  ___   _   _ 
   | |    / _ \ | '_ \ / _ \| __| / _ \ | '__\/ _ \ | | | |
   | |__ | (_) || |_) | (_) | |_ | (_) || |  | | | || |_| |
   |____| \___/ |_.__/ \___/ \__| \___/ |_|  |_| |_| \__, |
                                                      __/ |
    _____                                           _|___/ 
   /  __ \                                         | |              
   | /  \/  ___   _ __  _ __    ___   _ _    ___ _ | |_  _   ___   _ __  
   | |     / _ \ | '__|| '_ \  / _ \ | '__| / _ ' || __|(_) / _ \ | '_ \ 
   | \__/\| (_) || |   | |_) || (_) || |   | (_)  || |_ | || (_) || | | |
    \____/ \___/ |_|   | .__/  \___/ |_|    \__/|_|\___||_| \___/ |_| |_|
                       | |                                    
                       |_|                                    
""")

# -Nivel 1

print("\n Eres Gabriel Foreman, un investigador de Lobotomy Corporation. te encargas de la revision y el control de las anormalidades que crea la compañia en secreto. \n")
print("mientras pasas por los cuartos de contencion de cada anormalidad como es habitual, notas que el pasillo tiene un silencio inquietante al que no estas acostumbrado.")
print("pero el silecio es interrumpido por un grito desgarador a lo lejos, no sabes si es una anormalidad ya que nunca antes habias escuchado a alguna gritar asi.")
print("no sabes si arriesgarte a REVISAR o seguir tus isntintos y CORRER. Pero sabes que tienes que actuar rapido. \n")
    
opcion1 = input("¿que haces primero CORRER de ese lugar o ir a REVISAR? -> ").lower()

if opcion1 == "revisar":

    # -Nivel 2-(ruta de la curiosidad)

    print("\n entiendes que esto es parte de tu trabajo y podras lidiar con la situacion, asi que vas a revisar. \n")
    print("de camino te topas con que varios de los cuartos de contencion abiertos")
    print("y varias manchas de sangre que dan hacia el cuarto de control. Estas muy confundido y asustado.")
    print("Pero tambien te sientes acechado y escuchas pisadas que suenan en la oscuridad,")
    print("piensas en arriesgarte para avegiguar que paso en el cuarto de control o esconderte para que no te vea lo que te este asechando. \n")
    opcion2 = input("¿que haces, vas a ARRIESGARTE o a ESCONDERTE?-> ").lower()

    if opcion2 == "arriesgarte":

        # -Nivel 3

        print("\ncorres para llegar rapido al cuarto de control lleno de sangre y evitar que lo que este asechando no te atrape. \n")
        print("llegas al cuarto y cierras la puerta, lo unico que vez es una sala oscura con el guardia de desangrado en el suelo")
        print("pero te percatas que el guardia tiene una nota. \n")
        print("la nota muestra ordenes para abrir las puertas de todas las anormalidades, de parte de los altos mandos Lobotomy Corporation,")
        print("para limpiar las investigaciones ilegales echas alli.")
        print("antes de siquiera reacionar a la noticia, un anormalidad escondida en el techo te atraviesa el pecho con sus garras. \n")
        print("mueres travesado por la anormalidad, pero descubriendo el destino de todo tu trabajo y años de investigacion. \n")
        print("FIN DEL JUEGO.")

    elif opcion2 == "esconderte":

        print("\nsin pensarlo mucho, te escondes en uno de los cuartos de contencion abiertos, asegurandote que no alla nignuna anormalidad. \n")
        print("Y notas a eso que te acechaba, una anormalidad que ya habias estudiado con anterioridad")
        print("su gran peso y fuerza a pesar de tener el tamaño de un humano lo hace lento, podrias distraerlo facilmente para correr al ascensor y salir de ese lugar")
        print("tienes cerca tu libreta de anotaciones para lanzarla y distraer a la anormalidad o esperar a que la anormalidad se valla y irse con cuidado. \n")
        opcion3 = input("que haras, DISTRAER a la anormalidad o ESPERAR e ir con cautela?-> ").lower()

        if opcion3 == "esperar":

            # -Nivel 4

            print("\n aunque lenta, sigue siendo una anormalidad peligrosa, decides esperar a que te pierda el rastro. \n")
            print("despues de un rato la anormalidad se va y dejas de escucharla o sentirla, sales con cautela y te dirijes rapido al ascensor, pero habrias llegado tarde")
            print("ya que el cierre de seguridad fue ejecutado ahora todas las puertas y salidas estan cerradas, incluyendo el ascensor")
            print("corres para evitar que te vean mas anormalidades, encontrandote con unos conductos de aire, podrian llevarte al primer piso probablemente. \n")
            print("al viajar por los conductos llegas a un almacen, lo reconoces, en efecto es el primer piso, alparecer personas ya estan escondidas alli")
            print("bajas al almacen esperando ser resivido, y te resiven como superviviente ultil. Te proponen ir a encontrar una posible salida en la oficina del gerente")
            print("y el otro grupo no se quieren arriesgar a salir con anormalidades fuera. \n")
            opcion6 = input("¿con que grupo te quedas, con el grupo del ALMACEN o el grupo que va a la sala del GERENTE?-> ").lower()

            if opcion6 == "almacen":

                # - (Nievel 7)

                print("\n Decides quedarte en el almacen con los demas, mientras el resto de personas del grupo decidieron irse en busca de la salida. \n")
                print("la tension en el almacen aumentaba, pero uno de los empleados del piso 5 llamado Damian, se habria autoimpuesto el rol de lider")
                print("empezando a administrar tanto los materiales como suministros encontrados en el almacen y dirigiendo al resto del grupo \n")
                print("En un punto empezaron con pequeñas escurcieones afuera del almacen para encontrar algun tipo de ayuda para salir")
                print("sin suerte de encontrar algo. en uno de esos viajes encontraron una especie de anormalidad que nunca habias visto")
                print("capas tirar una especie de fluido que de ser consumido otorgaba una gran cantidad de energia. \n")
                print("En un punto todo el grupo lo consumia, para olvidarse del hambre y seguir buscando una salida")
                print("te negabas a consumir eso por miedo a los efectos secundarios, y tenias razon. Todos empezaron a transformarce en anormalidades")
                print("infectando a todo con el que tengan contacto, incluyendote. \n")
                print("tus recuerdos estan intactos pero no tienes voluntad, te guias por mero instinto vagando para siempre en esas olvidadas oficinas")

            elif opcion6 == "gerente":

                print("\n No puedes quedarte mucho tiempo alli, decides irte con el otro grupo a buscar la salida en sala del gerente. \n")
                print("Antes de salir se equipan con armas y recursos, dejando atras el almacen")
                print("pasando por los pasillos se encuentras con anormalidades, las evitan lo mas posible y llegan al ascensor con exito")
                print("viajando al ultimo piso. Al llegar los resive un cuarto oscuro con un visible desorden, parece como si hubieran irrumpido buscando algo")
                print("el grupo busca cualquier indicio del gerete o de una posible salida al exterior, encontrando al gerente muerto por disparo de bala")
                print("pero con unas llaves en la mano, y una ranura de llave en la pared. El gerente intento escapar pero alparecer alguien lo impidio")
                print("insertan la llave y el panel para quitar el sistema de seguridad del edificio es desbloqueado")
                print("pero derepente uno de los del grupo detectan a una especie de militares llendo hacia la oficina, podrian hacerles lo mismo que al gerente")
                print("tienes que decidir rapido, podrian salir de alli pero las anormalidades tambien. \n")
                opcion7 = input("que decides hacer SALIR a costa de la muerte de civiles en el exterior o buscar otra ALTERNATIVA rapida?-> ").lower()

                if opcion7 == "salir":
                        
                    print("\n Al precionar el boton para abrir las seguridad del edificio, todo se combierte en un caos, vez por la ventana a las anormalidades salir")
                    print(" y piensas en salir rapido para evitar ser atrapado por los militare. \n")
                    print("\n Vez una salida de emergencia al lado de la ventana abierta, finalmente sales junto con el pequeño grupo que te seguia")
                    print("haz logrado salir, pero a que costo las anormalidades se esparcen en segundos. Condenaste a la ciudad pero viviste un dia mas")
                            
                elif opcion7 == "alternativa":

                    print("\n es demasiada consecuencia, no vale la pena condenar a la ciudad para escapar. \n")
                    print("intentas buscar una alternativa antes de que lleguen los militares. Piensas en usar los recursos que que agarraron en el almacen")
                    print("preparando granadas en la puerta del gerente y preparandose para atacar a primera instancia de ver a los militares, de repente")
                    print("aparen los militares, las granadas explotan y atacan con lanzas caseras y pistolas con pocas balas")
                    print("pudieron abatir a algunos pero los militares al fondo estaban mas preparados, matando a todo el grupo. \n")
                    print("te escondes, pero los militares te encuentran y deciden llevarte fuera, tienes demasiada informacion como para morir")
                    print("seguiras trabajando para Lobotomy Corporation, pero ya no sera por un salario, sino por tu vida")

                else:
                    print("\n La presion de la desicion te consume, no logras decidir a tiempo y los militares llegan avribillando a todos en la oficina, inlcuyendote \n")

            else:
                print("\n no te convence ninguna opcion, prefieres salir por tu cuenta y buscar una salida, lamentablemente las anormalidades ya han rodeado todo el almacen y al abrir la puerta")
                print("terminan entrando y asesinando a todo el grupo \n")

        elif opcion3 == "distraer":

            print("\n Lanzas la libreta lo mas lejos que puedas de ti, llamando la atencion de la anormalidad. \n")
            print("corres lo mas rapido posible al ascensor, parece que la anormalidad no puede alcanzarte y logras entrar y cerrar el ascensor")
            print("estas asalvo por ahora, pero te das cuenta que solo puedes ir a 3 de los pisos superiores. \n")
            opcion4 = input("¿cual elijes, PRIMER piso, QUINTO piso o el ULTIMO piso?-> ").lower()

            if opcion4 =="quinto":

                # -Nivel 5

                print("\n Pocos pueden entrar al piso 5, pero por alguna razon te permite subir, debe de estar pasando algo raro. \n")
                print("al subir el piso 5 esta muy silencioso, pero escuchas una especie de conversacion provenientes de un cuarto de juntas")
                print("son militares discutiendo en el plan de incendiar la infrestructura del piso 5 y esparsir anormalidades en primer piso")
                print("haciendo parecer como un fallo de seguridad y enterrar para siempre los secretos de Lobotomy Corporation")
                print("antes de que te des cuenta las alarmas se encienden y los militares salen, te escondesa rapidamente en un cuarto de limpieza")
                print("asomandote por una rendija vez a uno de los militares preparando una fuga de gaz para explotar todo el piso 5")
                print("no puedes hacer nada, el piso explota emvolviendo tu cuerpo en fuego, mueres incinerado")
                print("FIN DEL JUEGO")

            elif opcion4 == "ultimo":

                print("\n El piso del gerente es axecible, en este momento tienes que reportarle lo sucedido al gerente.")
                print("al llegar y asomarte por la puerta antes de entrar a la oficina del gerente, vez a militares interrogando al gerente. \n")
                print("Para que les diga donde esta la alarma de emergencia y el panel de control de seguridad, no puedes creer que esto este pasando")
                print("esccuhas una especie de negociacion para que el gerente se quede con parte de las ganancias que se consiguen con las anormalidades")
                print("de Lobotomy Corporation a cambio de su silencio y el codigo para una especie de inteligencia artificial ultil para la compañia")
                print("uno de los militares encuentras la llave de acceso escondida, y aunque la inteligencia artificial sea util")
                print("los militares dijeron que saben de alguien que podria replicarla. Matan al gerente, encienden las alarmas y dejan la llave en su cadaver. \n")
                print("En momentos se dan cuenta de tu precencia y sin darte cuenta te capturan, dictando tu camino a otra sucursal de Lobotomy Corporation")
                print("te encirran en otro subsuelo como del que escapaste, sin opcion a renunciar ya que en el registro tu moriste en el incidente de Lobotomy Corporation")
                print("FIN DEL JUEGO")
                
            elif opcion4 == "primer":
                    
                print("\n Al llegar al primer piso, hay alarmas sonando y un monton de tranajadores acumulados en la puerta del edificio, queriendo escapar. \n")
                print("en ese instante las compuertas de seguridad se activaron cerrando por completo todo el edificio, ahora nadie puede salir")
                print("en ese momento de isteria colectiva, las anormalidades no tardaron en llegar y matar a todos los que puedan. \n")
                opcion5 = input("vez a un grupo de empleados corriendo de la masacre, ¿que eliges, SEGUIRLOS o irte SOLO?-> ").lower()


                if opcion5 == "solo":

                    # -Nivel 6

                    print("\nno le prestas atencion al grupo, decides ir por tu cuenta. \n")
                    print("corriendo por los pasillos del primer piso, buscas algun lugar para esconderte de las anormalidades o una posible salida de ese piso")
                    print("esta infestado todo, la mayoria de abitaciones estan infestadas de gritos y anormalidades")
                    print("pofin encuentras el grupo de antes encerrados en el almacen. Quieres entrar pero cerraron puerta por completo")
                    print("eres alcansado por una anormalidad tirandote acido, derritiendote lentamnete y muriendo. \n")
                    print("FIN DEL JUEGO.")

                elif opcion5 == "seguirlos":

                    print("\ndecides seguir al grupo, y llegan a un almacen que por suerte no hay indicios de anormalidades alli. \n")
                    print("todo el grupo esta asustado y alterado, no saben como saldran de esta.")
                    print("Una de las personas del grupos calma a todos y les habla de una posible salida en el piso del Gerente")
                    print("muchos se niegan a ir despues de ver lo que hay afuera y otra parte del grupo prefieren arriesgarse e ir. \n")
                    opcion6 = input("¿con que grupo te quedas, con el grupo del ALMACEN o el grupo que va a la sala del GERENTE?-> ").lower()

                    if opcion6 == "almacen":

                        # -Nivel 7

                        print("\n Decides quedarte en el almacen con los demas, mientras el resto de personas del grupo decidieron irse en busca de la salida. \n")
                        print("la tension en el almacen aumentaba, pero uno de los empleados del piso 5 llamado Damian, se habria autoimpuesto el rol de lider")
                        print("empezando a administrar tanto los materiales como suministros encontrados en el almacen y dirigiendo al resto del grupo \n")
                        print("En un punto empezaron con pequeñas escurcieones afuera del almacen para encontrar algun tipo de ayuda para salir")
                        print("sin suerte de encontrar algo. en uno de esos viajes encontraron una especie de anormalidad que nunca habias visto")
                        print("capas tirar una especie de fluido que de ser consumido otorgaba una gran cantidad de energia. \n")
                        print("En un punto todo el grupo lo consumia, para olvidarse del hambre y seguir buscando una salida")
                        print("te negabas a consumir eso por miedo a los efectos secundarios, y tenias razon. Todos empezaron a transformarce en anormalidades")
                        print("infectando a todo con el que tengan contacto, incluyendote. \n")
                        print("tus recuerdos estan intactos pero no tienes voluntad, te guias por mero instinto vagando para siempre en esas olvidadas oficinas")

                    elif opcion6 == "gerente":

                        print("\n No puedes quedarte mucho tiempo alli, decides irte con el otro grupo a buscar la salida en sala del gerente. \n")
                        print("Antes de salir se equipan con armas y recursos, dejando atras el almacen")
                        print("pasando por los pasillos se encuentras con anormalidades, las evitan lo mas posible y llegan al ascensor con exito")
                        print("viajando al ultimo piso. Al llegar los resive un cuarto oscuro con un visible desorden, parece como si hubieran irrumpido buscando algo")
                        print("el grupo busca cualquier indicio del gerete o de una posible salida al exterior, encontrando al gerente muerto por disparo de bala")
                        print("pero con unas llaves en la mano, y una ranura de llave en la pared. El gerente intento escapar pero alparecer alguien lo impidio")
                        print("insertan la llave y el panel para quitar el sistema de seguridad del edificio es desbloqueado")
                        print("pero derepente uno de los del grupo detectan a una especie de militares llendo hacia la oficina, podrian hacerles lo mismo que al gerente")
                        print("tienes que decidir rapido, podrian salir de alli pero las anormalidades tambien. \n")
                        opcion7 = input("que decides hacer SALIR a costa de la muerte de civiles en el exterior o buscar otra ALTERNATIVA rapida?-> ").lower()

                        if opcion7 == "salir":
                            
                            # -Nivel 8
                        
                            print("\n Al precionar el boton para abrir las seguridad del edificio, todo se combierte en un caos, vez por la ventana a las anormalidades salir")
                            print(" y piensas en salir rapido para evitar ser atrapado por los militare. \n")
                            print("\n Vez una salida de emergencia al lado de la ventana abierta, finalmente sales junto con el pequeño grupo que te seguia")
                            print("haz logrado salir, pero a que costo las anormalidades se esparcen en segundos. Condenaste a la ciudad pero viviste un dia mas")
                            
                        elif opcion7 == "alternativa":

                            print("\n es demasiada consecuencia, no vale la pena condenar a la ciudad para escapar. \n")
                            print("intentas buscar una alternativa antes de que lleguen los militares. Piensas en usar los recursos que que agarraron en el almacen")
                            print("preparando granadas en la puerta del gerente y preparandose para atacar a primera instancia de ver a los militares, de repente")
                            print("aparen los militares, las granadas explotan y atacan con lanzas caseras y pistolas con pocas balas")
                            print("pudieron abatir a algunos pero los militares al fondo estaban mas preparados, matando a todo el grupo. \n")
                            print("te escondes, pero los militares te encuentran y deciden llevarte fuera, tienes demasiada informacion como para morir")
                            print("seguiras trabajando para Lobotomy Corporation, pero ya no sera por un salario, sino por tu vida \n")

                        else:
                            print("\n La presion de la desicion te consume, no logras decidir a tiempo y los militares llegan avribillando a todos en la oficina, inlcuyendote \n")

                    else:
                        print("\n no te convence ninguna opcion, prefieres salir por tu cuenta y buscar una salida, lamentablemente las anormalidades ya han rodeado todo el almacen y al abrir la puerta")
                        print("terminan entrando y asesinando a todo el grupo \n")

                else:
                    print("\n no sabes que hacer para sobrevivir, asi que una anormalidad termina ayudandote a decidir. Eres empalado por las garras de la anormalidad \n")

            else:
                print("\n intentas algun piso que nosea los que te permite ir, pero termina callendose el ascensor por una explocion proveniente del piso 5, caes inevitablemente a tu muerte \n")

        else:
            print("\n por el miedo decides no hacer nada, la anromalidad en algun punto te encontrara pero rezas para que no se asi. termina encontrandote despues de un rato y te asesina \n")

    else:
        print("\n te congelas por lo tetrica que es la escena ante tus ojos, terminas siendo alcanzado por la anomalia y te decapita. Ya no puedes saber que sucede \n")

# -Nivel 2-(ruta del instinto)

elif opcion1 == "correr":

    print("\n El miedo puede contigo, realmente no crees que sea tu compañero gastandote un broma. Vas corriendo lo mas rapido posible al ascensor y te dirijes al primer piso. \n")
    print("Actuas como si nada pasara para no llamar la atencion. No te importa si tu trabajo corre peligro, ahora prefieres vivir un dia mas.")
    print("En la salida te encuentras con unos soldados que te reconocen, llevandote adentro del edificio otra vez, amenasandote con un arma")
    print("no sabes quienes son o porque estan aqui despues de lo que acaba de pasar alla abajo, pero sabes que nada bueno saldra de eso, tienes que allar la forma de escapar")
    print("pasan por la zona de desinfectacion, podrias aprovechar el humo para robarle el arma al militar o tal vez esperar a ver donde te llevan para porbar una opcion menos arriesgada.\n")
    opcion2 = input("que estrategia eliges, ROBAR el arma o ESPERAR un momento menos arriesgado?-> ").lower()
    
    if opcion2 == "esperar":

        print("decides essperar y no planear ninguna escapada heroica, en momentos el militar te coloca una bolsa en la cabeza y te noquea.")
        print("despiertas en una sala llena de cuartos de contencion de anormalidades, como estabas acostumbrado a trabajar.")
        print("eres obligado a trabajar a punta de pistola por los militares y altos mandos de Lobotomy corporation hasta terminar su proyecto al que llaman: Angel")
    
    elif opcion2 == "robar":

        # -Nivel 3

        print("\n decides robar el arma, nisiquiera sabes que quieren de ti no puedes perder mas tiempo. \n")
        print("El gas decinfectante aparece, rapidamente te volteas y pateas al militar a tus espaldas agarrando su arma. Le pides explicaciones de quienes son y a donde te llevan")
        print("el militar te dice que vienen a llevarte a un lugar mas seguro, sus palabras suenan ensayadas, un tanto roboticas y cada vez se acerca mas a ti intentando intimidarte")
        print("tu subconciente te pide jalar el gatillo, pero no eres de matar gente, solo anormalidades. podrias llegar a escapar una vez las puertas se habran pero debes ser rapido.\n")
        opcion3 = input("que haces, MATAR al militar o ESCAPAR lo mas rapido que puedas?-> ").lower()

        if opcion3 == "matar":

            # -Nivel 4

            print("\n le disparas en la cabeza al militar por precion, su cuerpo se desploma en el suelo. Te quedas inmovil por lo acaba de pasar, tienes sangre salpicada en tu cara y manos. \n")
            print("No puedes perder mas tiempo a pezar del shock, el ruido seguramente alerto a otros militares. Agarras la llave de axceso que tenia el cuerpo y su radio rapidamente")
            print("y sales al siguiente pasillo, notas que la llave de axceso dice, Habitacion N36, nunca habias visto una habitacion con ese numero.")
            print("podria darte respuestas de lo que esta pasando, pero tambien deberias irte de alli antes de que te agarren los militares atraidos por el ruido del disparo. \n")
            opcion4 = input("planeas ir a la HABITACION desconocida o IRTE de alli lo mas rapido posible?-> ").lower()

            if opcion4 == "irte":

                # -Nivel 5

                print("\n justo cuando decides irte, las alarmas de seguridad suenan, cerrando toda salida y entrada del edificio. \n")
                print("mientras las alarmas suenan las puertas a tu alrededor se abren y empiezan a salir una especie de anormalidades incompletas ")
                print("aunque incompletas siguen siendo una canidad enorme de ellas, haciendo las igual de peligrosas. Cuando habran echo estas anromalidades sin tu supervision?. \n")
                print("No es tiempor de preguntarse eso, corres por los masillos antes de que se cierren por completo llegando a un habitacion muy oscura y la puerta se cierra atras de ti")
                print("no vez nada pero si escuchas una especie de respiracion frente de ti, las luces se encienden y muentran a una anormalidad gigante en medio de la habitacion")
                print("haces lo que puedes para evitar ser asesinado por ella, pero es imposible la anormalidad te atrapa y te debora. Sorprendentemente sigues con vida pero en su interior")
                print("encuetras a otros sujetos de pueba que han sido tragados, esta anormalidad es usada como una sala de tortura adentro de ella")
                print("no puedes escapar y te quedas atrapado hasta morir de hambre")
                print("Fin del juego\n")

            elif opcion4 == "habitacion":

                print("\n intentas buscarla siguiendo el pasillo N30, hasta que das con la habitacion. \n")
                print("la llave de axceso funciona y abre la puerta, encuentras un monton de documentos, la mayoria de ellos habla de espias internos de la compañia que intentan averiguar las investigacion")
                print("secretas que oculta la empreza y demostrar que la inteligencia artificial que se esta desarrollando esta creada para administrar estas investigaciones y encontrar una forma de crear")
                print("energia mediante el desarrolo de anormalidades con esas caracteristicas, te han estado ocultando todo eso para en algun punto usarte como chibo expiatorio")
                print("tienes que agarrar estos documentos y revelar el secreto para evitar que te utilicen. Antes de actuar suena una alarma de seguridad que te lleva a actuar rapido.")
                print("agarras los documentos y sales de la habitacion rapido, muchos pasilos estan cerrados pero quedan dos aun abiertos.\n")
                opcion5 = input("Rapido cual elijes, el de la IZQUIERDA o el de la DERECHA?-> ").lower()

                if opcion5 == "derecha":

                    # -Nivel 6

                    print("\n en la derecha encuentras a un grupo corriendo a un almacen para esconderse de las anormalidades. \n")
                    print("entrando al almacen el grupo te pregunta, que son los documentos que tienes en la mano. Le explicas los secretos de la empresa y su plan para ocultarnos")
                    print("convenciendo a las personas con miedo a salir, para juntar fuerzas y logran salir para revelar la verdadera cara de Lobotomy Corporation. \n")
                    print("haciendoce paso atravez de las anormalidades y llegando al ultimo piso. Tomaron por sorpresa a los militares que se encontraban en la oficina del gerente")
                    print("superandolos en numero los abaten a todos, viendo al gerente ya muerto. le quitan la clave para abrir a la salida. \n")
                    print("tu grupo a logrado escapar y reportar lo ocurrido en la empresa a la prensa. Lobotomy Corporation fue vencida por la fuerza de sus propios empleados \n")

                elif opcion5 == "izquierda":

                    print("\n te encuentras con un monton de anormalidades llendo a la sala principal del edificio junto con muchos gritos de empleados.")
                    print("imposible ir al ascensor para escapar. Tienes que tomar una salida alternativa. \n")
                    opcion6 = input("la SALIDA de incendios parece que aun no esta cerrada o puedes ir por las ESCALERAS para llegar al ultimo piso donde podria haber una salida-> ").lower()

                    if opcion6 == "salida":

                        # -Nivel 7

                        print("vas por la salida de incendios, pero era una trampa militares y agentes estaban esperando a empleados que vayan por alli para llevarselos.\n")
                        print("Desgraciadamente tu fuiste uno de ellos, te quitan los documentos y te meten a una caminota con los ojos vendados, quien sabe a donde te llevaran")
                        print("pero es seguro que de estas ya no podras escapar\n")
                        print("FIN DEL JUEGO\n")

                    elif opcion6 == "escaleras":

                        print("\n La salida del ultimo piso en la oficina del jefe es la mas segura, mejor usar las escaleras.\n")
                        print("te acercas a al ultimo piso evitando rapidamente un especie de fuga de gaz en el piso 5. llegas al ultimo piso y vez a soldados saliendo de la oficina")
                        print("en poco tiempo descubres porque estaban alli, vez al jefe agonizando en el piso, y te dice que tu puedes destruir a la compañia para siempre. \n")
                        print("Te entrega un USB con un nombre escribo, Angel, te pide que junto con las pruebas que tienes reveles todo a la prensa. te abre la salida de emergencia")
                        print("te pide que apenas salgas te escondas cerca de la sucursal rival para evitar ser capturado por los militares. no puedes perder mas tiempo y te despides del gerente")
                        print("sales del edificio evitando a los militares que estan fuera. Lograste escapar de una posible muerte o sufrimiento interminable. \n")
                        print("Ahora todos sabran que es Lobotomy Corporation \n")

                    else:
                        print("\n te congelas intentando decidir, las anormalidades te encuentran y eres incapas de evitar a todas. eres asesinado por ellas como los otros empleados \n")

                else:
                    print("\n no sabes a cual ir a si que terminas desviandote a otro camino, quedas encerrado por dos puertas que se activan con movimiento. Nadie sabe que estas alli dudas que te encuentres pronto")

            else:
                print("\n te tardas decidiendo y terminan llegando muy rapido los militares, te atrapan y amordasan para que no escapes mas. llevandote a una camioneta en direccion a algun lugar \n")

        elif opcion3 == "escapar":

            # -Nivel 4-(alternativa)

            print("\n Le lanzas el arma al militar distrallendolo para escapar por la pruerta que ya se abierto.\n")
            print("Siendo perseguido por el guardia logras ser un poco mas rapido pero llegas a un pasillo sin salida con una ventana al exterior, y al lado una puerta ermetica medio abierta. \n")
            opcion4 = input("no puedes quedarte pensando que elijes, saltar por la VENTANA esperando no romperte tantos huesos como para escapar o cruzar la PUERTA sin saber que hay dentro?-> ")


            if opcion4 == "puerta":

                # -Nivel 5-(alternativa)

                print("\n Al cruzar la puerta la cierras tras de ti para evitar al militar. No vez nada esta todo oscuro, solo vez una computadora al final de la abitacion. \n")
                print("la computadora es muy grande y avanzada para estar en un cuarto tan oculto. Te saluda una inteligencia artificial que se presenta como Angel")
                print("no puedes creer que allan trabajado en algo tan avanzado en secreto. La inteligencia artificial te dice que no puedes estar alli todabia ya que tu mente aun no esta corrompida")
                print("confundido le preguntas a que se refiere y te explica que ella es creada en base a mentes de empleados entrenados que an pasado por momentos traumatico")
                print("para que ella absorbe los sentimientos mas fuertes del ser humano y poder dirigir y entender a las anormalidades que tienen un funcionamiento parecido a ella. \n")
                print("y tu estas en la lista de mentes a utilizar, pero al ser revelada la informacion de Angel ya no sirves por tener algo de humanidad en ti aun")
                print("una anormalidad sale de la oscuridad asesinadote por ordenes de Angel")
                print("FIN DEL JUEGO")

            elif opcion4 == "ventana":

                print("\n Tomas impulso y saltas destrosando la ventana y llegando a un techo bajo que estaba del otro lado de la ventana.")
                print("corres por los techos intentando perder al militar, hasta llegar a un callejon, te escondes y parece que ya lo haz perdido")
                print("no sabes que va a pasar o que sucedio alli adentro, pero tienes que uir porque te estaran buscando")

            else:
                print("\n te detienes en seco no sabes que hacer, ya es muy tarde para elejir el militar de detiene de un disparo en la pierna, y te desmayas\n ")

        else:
            print("\n te congelas en frente del militar, el te arrebata el arma y te noquea de un golpe para luego encerrarte en una camineta de Lobotomy Corporation. Quien sabe a donde te llevara \n")

    else:
        print("\n no terminas de saber que hacer, pero por instinto intentas patear al militar. Jalando por axidente su gatillo y disparandote a ti mismo \n")

else:
    print("\n te quedas pensando por un buen rato congelado, intentando desifrar que fue eso. Pero eres alcanzado por el ataque de una anormalidad que alparecer a escapado.\n")