function Detect_ir () {
    let Couleur_min = 0
    if (crickit.signal1.analogRead() < Couleur_min) {
        crickit.signal1.digitalWrite(true)
    } else if (crickit.signal8.analogRead() < Couleur_min) {
        crickit.signal8.digitalWrite(true)
    } else {
        crickit.signal1.digitalWrite(false)
        crickit.signal8.digitalWrite(false)
    }
}
// Fonction pour simuler la détection d'une citerne
function detectCiterne () {
    // Simule la détection de citerne (remplacer cette fonction par le vrai capteur)
    if (crickit.signal4.digitalRead()) {
        // Simule la détection 20 % du temps
        return true
    }
    return false
}
// Fonction pour suivre la ligne noire avec les capteurs tactiles
function followLine () {
    irLeft = crickit.signal1.analogRead()
    irRight = crickit.signal8.analogRead()
    // Utiliser les capteurs tactiles pour guider les moteurs
    if (irLeft && !(irRight)) {
        // Tourne légèrement à gauche
        crickit.motor1.run(50)
        // Moteur gauche plus lent
        crickit.motor2.run(100)
    } else if (irRight && !(irLeft)) {
        // Moteur droit à pleine vitesse
        // Tourne légèrement à droite
        crickit.motor1.run(100)
        // Moteur gauche à pleine vitesse
        crickit.motor2.run(50)
    } else {
        // Moteur droit plus lent
        // Avancer tout droit
        crickit.motor1.run(100)
        // Pleine vitesse pour les deux moteurs
        crickit.motor2.run(100)
    }
}
// Fonction pour déposer les billes
function dropBilles () {
    crickit.servo1.setAngle(90)
    // Ouvre la trappe
    pause(1000)
    // Attendre 1 seconde
    crickit.servo1.setAngle(0)
    pause(5000)
}
music.baDing.play()
crickit.motor1.run(0)
crickit.motor2.run(0)
irRight = 0
let irLeft = crickit.touch1
let irRight = crickit.touch2
basic.forever(function on_forever() {
    followLine()
    //  Suivre la ligne noire avec les capteurs tactiles
    if (detectCiterne()) {
        //  Si une citerne est détectée
        crickit.motor1.stop()
        //  Arrêter le moteur gauche
        crickit.motor2.stop()
        //  Arrêter le moteur droit
        dropBilles()
        //  Déposer les billes
        pause(2000)
    }
    
})
