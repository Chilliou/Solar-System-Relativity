class Planet:
    def __init__(self, nom, masse, rayon, vitesse, pos_x, rgb , pos_y =0 ) -> None:
        self.nom = nom
        self.masse = masse
        self.rayon = rayon
        self.vitesse = vitesse
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rgb = rgb
    
    def __str__(self) -> str:
        """Affiche une représentation textuelle de l'objet Planète."""

        # Maximum width for the name (dynamically adjusted)
        nom_width = len(self.nom)

        # Fixed width for other columns
        col_width = 10

        # Header
        en_tete = f"+{'-' * (nom_width + 4 * col_width + 6)}+"
        lignes = [en_tete]

        # Content (formatted with appropriate conversion)
        ligne1 = f"| {self.nom:^{nom_width}s} |"
        ligne2 = f"| {'masse :':<{col_width}s} {self.masse:.2e} |"  # Use exponential notation for large mass
        ligne3 = f"| {'rayon :':<{col_width}s} {self.rayon:.2f} |"  # 2 decimal places for radius
        ligne4 = f"| {'vitesse:':<{col_width}s} {self.vitesse:.4f} |"  # 4 decimal places for velocity (consider scientific notation if needed)
        ligne5 = f"| {'pos_x  :':<{col_width}s} {self.pos_x:.4f} |"  # 4 decimal places for position (adjust as needed)
        ligne6 = f"| {'pos_y  :':<{col_width}s} {self.pos_y:.4f} |"  # 4 decimal places for position (adjust as needed)
        lignes.extend([ligne1, ligne2, ligne3, ligne4, ligne5, ligne6])

        # Footer
        pied = f"+{'-' * (nom_width + 4 * col_width + 6)}+"
        lignes.append(pied)

        return "\n".join(lignes)
