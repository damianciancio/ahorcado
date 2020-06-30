Feature: Ahorcado functionality
    Scenario: letter input
    Given a new hanged game starting with hello word 
    When i input "p"
    Then i get an error message

    Scenario: word input
    Given a new hanged game starting with hello word 
    When i input "hola"
    Then i will be redirect to the winning page
    
    Scenario: number of attempts
    Given a new hanged game starting with hello word 
    When i input "r"
    Then i will have "6" number of attempts remaining

    Scenario: testing hanged game browser
    Given a new hanged game
    When i enter the browser
    Then Then i should have a title "Ahorcado" 