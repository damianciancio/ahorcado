Feature: Funcionalidad de Ahorcado
    Scenario: Ingreso de letra incorrecta
    Given el comienzo de un nuevo juego con la palabra hola
    When ingreso p
    Then obtengo un mensaje de error

    Scenario: Ingreso de palabra
    Given el comienzo de un nuevo juego con la palabra hola
    When ingreso hola
    Then gano la partida

    Scenario: Ingreso letra correcta
    Given el comienzo de un nuevo juego con la palabra hola
    When ingreso o
    Then obtengo un mensaje de acierto

    Scenario: Intentos restantes
    Given el comienzo de un nuevo juego con la palabra hola
    When ingreso p
    Then me quedan 6 intentos restantes