use std::io;
use rand::{self, seq::SliceRandom};

fn main() {
    // Pour pouvoir les réutiliser
    let mut rng = rand::thread_rng();
    let stdin = io::stdin();
    // On mélange la liste de départ pour qu'il n'y a pas d'influence de l'ordre de la liste
    let mut classement = ["Ginette MPSI I", "LLG MPSI I", "LLG MPSI DP", "LLG MP2I I", "LLG MP2I DP", "Stan MPSI I", "Stan MPSI DP", "H4 MPSI I", "H4 MPSI DP", "Hoche MPSI I", "Hoche MPSI DP", "Hoche MP2I I", "Hoche MP2I DP", "StLouis MPSI I", "StLouis MPSI DP", "StLouis MP2I I", "StLouis MP2I DP", "Berthelot MPSI I", "Berthelot MPSI DP", "JdS MPSI I", "JdS MPSI DP", "JdS MP2I I", "JdS MP2I DP", "Michelet MPSI I", "Michelet MPSI DP", "Charlemagne MPSI DP", "Condorcet MPSI DP", "Fénelon MPSI DP", "Fénélon StM MPSI DP", "Fénélon StM MP2I DP", "Chaptal MPSI I", "Chaptal MP2I DP"];
    classement.shuffle(&mut rng);

    loop {
        let mut swapped = false;
        // On fait un bubble sort pour passer par un max de comparaison et avoir un classement
        // satisfaisant
        for n_elem in 0..(classement.len()-1) {
            println!("1) {}", classement[n_elem]);
            println!("VS");
            println!("2) {}", classement[n_elem+1]);
            let mut answer = String::new();
            stdin.read_line(&mut answer).unwrap();
            if answer.trim() == "2" {
                classement.swap(n_elem, n_elem+1);
                swapped = true;
            }
            println!();
        }
        if !swapped { break; }
    }
    for elem in classement {
        println!("{}", elem);
    }
}
