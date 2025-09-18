# Python Script: 1b
# Filename: translations.py

# Description:
# Module containing dictionaries to change the language between Greek and English

from dash import html, dcc
import dash

# Language dictionary for the home page
translations_homepage = {
    "el": {
        "title": "Καλωσήρθατε στο CompactStarsLab",
        "subtitle": "Μια διαδραστική εφαρμογή για την εξερεύνηση ιδιοτήτων των Συμπαγών Αστέρων",
        "language_label": "Γλώσσα",
        "explore_general": "Γενικά",
        "explore_composition": "Σύνθεση ύλης",
        "explore_eos": "Καταστατικές Εξισώσεις",
        "explore_tov": "Επίλυση εξισώσεων TOV"
    },
    "en": {
        "title": "Welcome to CompactStarsLab",
        "subtitle": "An interactive tool for exploring properties of Compact Stars",
        "language_label": "Language",
        "explore_general": "General info",
        "explore_composition": "Composition of Matter",
        "explore_eos": "Equations of State",
        "explore_tov": "Solving TOV equations"
    }
}

# Language dictionary for the general page
translations_generalpage = {
    "el": {
        "back_to_home": "Αρχική",
        "general_title": "Γενικές πληροφορίες για Συμπαγείς Αστέρες",
        "general_intro": "Σε αυτή τη σελίδα μπορείτε να βρείτε γενικά στοχεία για συμπαγείς αστέρες.",
    },
    "en": {
        "back_to_home": "Home",
        "general_title": "General info for Compact Stars",
        "general_intro": "On this page you can find general info for Compact Stars.",
    }
}

# Language dictionary for the composition page
translations_compositionpage = {
    "el": {
        "back_to_home": "Αρχική",
        "composition_title": "Σύνθεση ύλης",
        "composition_intro": "Σε αυτή τη σελίδα μπορείτε να εξερευνήσετε την σύνθεση της ύλης στο εσωτερικό συμπαγών αστέρων.",
    },
    "en": {
        "back_to_home": "Home",
        "composition_title": "Composition of matter",
        "composition_intro": "On this page, you can explore the composition of matter inside compact stars.",
    }
}

# Language dictionary for the eos page
translations_eospage = {
    "el": {
        "back_to_home": "Αρχική",
        "eos_title": "Καταστατικές Εξισώσεις",
        "eos_intro_1": "Η καταστατική εξίσωση (EOS) αποτελεί το τελευταίο αλλά ουσιώδες κομμάτι του παζλ στην περιγραφή ενός Συμπαγή Αστέρα. Μέσω αυτής καθορίζεται η σχέση μεταξύ της πίεσης "+
        "και της ενεργειακής πυκνότητας της ύλης, και κατ\' επέκταση οι ιδιότητες της ύλης από την οποία αποτελείται το άστρο. "+"Η καταστατική εξίσωση απορρέει από τον Πρώτο Νόμο της Θερμοδυναμικής και "+
        "περιγράφει τη φυσική πέρα από τη βαρύτητα, τη κβαντική φυσική της ύλης. Ο συνήθης φορμαλισμός δίνεται παρακάτω:",
        "eos_intro_2": "$P=P(\epsilon)$ ή $\epsilon=\epsilon(P)$",
        "eos_intro_3":"καθιστώντας την καταστατική εξίσωση μια ***βαροτροπική*** εξίσωση. Σε αυτή τη σελίδα μπορείτε να εξερευνήσετε διάφορες καταστατικές εξισώσεις για διαφορετικούς τύπους Συμπαγών Αστέρων, μέσα από διαδραστικά widgets.",
        "NS_button_1": "Αστέρες Νετρονίων: Κρούστα",
        "NS_button_2": "Αστέρες Νετρονίων: Πυρήνας",
        "NS_button_3": "Αστέρες Νετρονίων: Πολυτροπικές εξισώσεις",
        "QS_button": "Αστέρες Quark"
    },
    "en": {
        "back_to_home": "Home",
        "eos_title": "Equations of State",
        "eos_intro_1": "The equation of state (EOS) is the final but essential piece of the puzzle in describing a Compact Star. It establishes the relation between the pressure and energy density of matter, "+
        "and, by extension, the properties of the matter of which the star is composed. "+"The equation of state derives from the First Law of Thermodynamics and describes physics beyond gravity, "+
        "the quantum physics of matter. The commonly used formalism is shown below:",
        "eos_intro_2": "$P=P(\epsilon)$ or $\epsilon=\epsilon(P)$",
        "eos_intro_3": "rendering the equation of state a ***barotropic*** one. On this page you can explore various equations of state for different types of Compact Stars, through interactive widgets.",
        "NS_button_1": "Neutron Stars: Crust",
        "NS_button_2": "Neutron Stars: Core",
        "NS_button_3": "Neutron Stars: Polytropic equations",
        "QS_button": "Quark Stars"
    }
}

# Language dictionary for the eos widgets of Neutron Stars
translations_eos_widgets_NS = {
    "el": { "Default_widget_message": "⚙️ Παρακαλώ επιλέξτε ένα widget για να πειραματιστείτε.",
            "core": "ΠΥΡΗΝΑΣ",
            "layer": "ΣΤΡΩΜΑ ΚΡΟΥΣΤΑΣ",    
        "widget_1": {   "title": "Widget 1: Περιγράφοντας τη δομή ενός Αστέρα Νετρονίων I",
                        "subtitle": "Κατά την ανάλυση, ο Αστέρας Νετρονίων θεωρείται ότι αποτελείται από δύο μέρη: την ΚΡΟΥΣΤΑ (εξωτερικά) και τον ΠΥΡΗΝΑ (εσωτερικά). Κάθε μέρος περιγράφεται από την αντίστοιχη καταστατική εξίσωση.",
                        "section": "Η ΚΡΟΥΣΤΑ",
                            "text": "Η **κρούστα** ενός Αστέρα Νετρονίων αποτελείται από **τέσσερα στρώματα**. Η καταστατική της εξίσωση είναι γνωστή και καλώς ορισμένη. Μετακινηθείτε πάνω στη καμπύλη ενός στρώματος για να δείτε τον τύπο της καταστατικής του εξίσωσης και να τονίσετε το γράφημα της, "+
                            "όπως επίσης και για να επισημάνετε την περιοχή του στρώματος στην 2D απεικόνιση του αστέρα.",
                            "graph1_title": ">Λεπτομερής Καταστατική Εξίσωση Κρούστας: ε<sub>crust</sub>(P)",
                            "graph2_title": ">Σχηματική 2D απεικόνιση της δομής ενός Αστέρα Νετρονίων",
                            "message_title": "**>>Πληροφορίες**",
                            "message_region": "-Βρίσκεστε στην περιοχή: ",
                            "message_region_eos": "-Καταστατική εξίσωση: ",
                            "message_p_range": "-Εύρος πίεσης P: ",
                            "star_mass_slider": "**>>Μάζα Αστέρα Νετρονίων**"+r" ($M_\odot$)" 
        },
        "widget_2": {   "title": "Widget 2: Περιγράφοντας τη δομή ενός Αστέρα Νετρονίων II",
                        "subtitle": "Κατά την ανάλυση, ο Αστέρας Νετρονίων θεωρείται ότι αποτελείται από δύο μέρη: την ΚΡΟΥΣΤΑ (εξωτερικά) και τον ΠΥΡΗΝΑ (εσωτερικά). Κάθε μέρος περιγράφεται από την αντίστοιχη καταστατική εξίσωση.",
                        "section": "Ο ΠΥΡΗΝΑΣ",
                            "text": "Ο **πυρήνας** ενός Αστέρα Νετρονίων παρουσιάζει με τη σειρά του ιδιαίτερο ενδιαφέρον. Στην απλούστερη περίπτωση, ο πυρήνας αντιμετωπίζεται ως ένα ενιαίο στρώμα και περιγράφεται με μια καταστατική εξίωση. "+
                            "Ωστόσο, εφόσον η ακριβής σύνθεση του πυρήνα του άστρου παραμένει άγνωστη, το ίδιο άγνωστη είναι και η καταστατική του εξίσωση. Υπάρχουν διάφορα θεωρητικά μοντέλα που επιχειρούν να αναδείξουν τον σωστό φορμαλισμό. "+
                            "Παρακάτω, παρουσιάζουμε τις γραφικές παραστάσεις για 21 \"κύρια\" τέτοια μοντέλα καταστατικών εξισώσεων. Επιλέξτε ένα μοντέλο για να δείτε τον αντίστοιχο τύπο της καταστατικής εξίσωσης και για να δείτε τη γραφική της παράσταση σε ξεχωριστό γράφημα.",
                            "graph1_title": ">Μοντέλα για την Καταστατική Εξίσωση του Πυρήνα: ",
                            "graph1_memo": ">Υπόμνημα",
                            "graph1_memo_text_caus": " μη παραβίαση της αιτιότητας: ",
                            "graph1_memo_text_no_caus": " παραβίαση της αιτιότητας: ",
                            "graph1_memo_checklist": " (κάνε πιο έντονο αυτό το μέρος των καμπυλών)",
                            "graph1_memo_text_eostype1": "**>>Μορφή 1**",
                            "graph1_memo_text_eostype2": "**>>Μορφή 2**",
                            "graph1_memo_text_genformula": "**Γενικός τύπος: **",
                            "graph1_memo_text_models": "**Μοντέλα: **",
                            "model_select_title": ">Επιλογή συγκεκριμένου μοντέλου για την καταστατική εξίσωση του πυρήνα: ",
                            "model_select_choice": "**>>Μοντέλο:  **",
                            "model_select_fullname": "**>>Πλήρες όνομα:  **",
                            "model_select_type": "**>>Μορφή:  **",
                            "model_select_formula": "**>>Τύπος:  **",
                            "graph2_title": ">Γραφική παράσταση επιλεγμένου μοντέλου: "
    },
    "widget_3": {       "title": "Widget 3: Τεχνητή δημιουργία εξισώσεων (πολυτροπικές και γραμμικές καταστατικές εξισώσεις)",
                        "subtitle": "Στην απλούστερη περίπτωση, όπου ένα από τα 21 \"κύρια\" μοντέλα καταστατικών εξισώσεων χρησιμοποιείται για τον πυρήνα, "+
                        "η συνολική καταστατική εξίσωση του Αστέρα Νετρονίων δίνεται από τη σχέση:",
                        "total_eos_form": r"""
                        $
                        \epsilon(P)=
                        \begin{cases}
                        \epsilon_{crust}(P), & P<P_{crust-core} \\
                        \epsilon_{main}(P), & P\geq P_{crust-core}
                        \end{cases}
                        $
                        """,
                        "subtitle_2": "όπου η καταστατική του πυρήνα είναι: ",
                        "core_eos_form_main": r"$\epsilon_{core}(P)=\epsilon_{main}(P)$",
                        "subtitle_3": r"""και η οριακή πίεση $P_{crust-core}$ είναι $0.696$ $MeV\cdot fm^{-3}$ για την ***PS*** καταστατική εξίσωση και """+
                        r"""$0.184$ $MeV\cdot fm^{-3}$ για τις υπόλοιπες "κύριες" καταστατικές εξισώσεις.""",
                        "section_1": "ΤΟ ΠΟΛΥΤΡΟΠΙΚΟ ΠΛΕΓΜΑ",
                            "sec1_show_method_btn": "Εμφάνιση μεθοδολογίας",
                            "sec1_text_poly1": "Κάποιες φορές, τα 21 \"κύρια\" μοντέλα για την καταστατική εξίσωση του πυρήνα, δεν είναι αρκετά. Ειδικότερα, "+
                            r"ορισμένες μελέτες απαιτούν (ιδιαιτέρως) λεπτομερή και πυκνή κάλυψη και δειγματοληψία των χώρων $M-R$ και $\epsilon-P$, κάτι το οποίο δεν επιτυγχάνεται με την χρήση μόνο των 21 "+ "\"κύριων\" μοντέλων. "+
                            "Σε αυτές τις περιπτώσεις, διάφορες στρατηγικές μπορούν να εφαρμοστούν, για την τεχνητή δημιουργία ενός ικανοποιητικά μεγάλου αριθμού καταστατικών εξισώσεων. Στο συγεκριμένο *widget* μπορείτε να εξερευνήσετε την μεθοδολογία των **πολυτροπικών εξισώσεων** και να κατασκευάσετε **πολυτροπικά πλέγματα**.",
                            "sec1_text_poly2": "Η μεθοδολογία των πολυτροπικών εξισώσεων χωρίζει τον **ΠΥΡΗΝΑ** του Αστέρα Νετρονίων σε δύο στρώματα. Το **πρώτο στρώμα** εκτείνεται στην περιοχή πίεσης: "+r"$P\in [P_{crust-cote},P_0]$ (ή ισοδύναμα στην περιοχή πυκνότητας μάζας: $\rho \in[\rho_{crust-core},\rho_0]$) και διαθέτει ένα από τα "+
                            "\"κύρια\" μοντέλα ως καταστατική εξίσωση. Το **δεύτερο στρώμα** εκτείνεται στην περιοχή πίεσης: "+r"$P\in[P_0,P_n]$ (ή ισοδύναμα στην περιοχή πυκνότητας μάζας: $\rho \in[\rho_0,\rho_n]$). Αυτό το στρώμα χωρίζεται σε $n$ πολυτροπικά τμήματα, καθένα από τα οποία χαρακτηρίζεται από μια ξεχωριστή πολυτροπική σχέση "+
                            "μεταξύ της πίεσης και της ενεργειακής πυκνότητας. Η συνολική εξίσωση κατάστασης του δεύτερου στρώματος είναι μια τμηματική συνάρτηση που συνδυάζει όλες αυτές τις διακριτές πολυτροπικές σχέσεις. "+r"Οι τιμές $P_0$ και $P_n$ (ή ισοδύναμα $\rho_0$ και $\rho_n$) επιλέγονται αυθαίρετα. Συνήθως, επιλέγεται η πυκνότητα πυρηνικού κορεσμού ως αφετηρία: $\rho_0=\rho_{sat}$.",
                            "sec1_text_poly3a": r"Σε κάθε πολυτροπικό τμήμα $(\rho_{i-1}\leq\rho\leq\rho_i)$, συναντάμε την παρακάτω σχέση ανάμεσα στην πίεση και την ενεργειακή πυκνότητα",
                            "sec1_text_poly3b": r"όπου η τιμή της σταθεράς $K_i$ προσδιορίζεται από την πίεση και την πυκνότητα μάζας στο προηγούμενο σημείο αναφοράς ως εξής",
                            "sec1_text_poly3c": r"και ο πολυτροπικός δείκτης του τμήματος $\Gamma_i$, υπολογίζεται ως εξής",
                            "sec1_text_poly3d": r"Η τιμή του $\Gamma_i$ σε κάθε τμήμα επιλέγεται συνήθως αυθαίρετα.  Για $\Gamma_i\neq1$, η σχέση μεταξύ της πίεσης και της ενεργειακής πυκνότητας των τμημάτων έχει ως εξής",
                            "sec1_text_poly3e": r"ενώ για $\Gamma_i=1$, η αντίστοιχη σχέση είναι",
                            "sec1_text_poly4a": r"Η διαίρεση σε πολυτροπικά τμήματα, γίνεται με τέτοιο τρόπο ώστε τα τμήματα να είναι ισομήκη στον λογάριθμο της πυκνότητας ($\log{\rho$}). Από την διαίρεση προκύπτουν οι τιμές της πυκνότητας $\rho_i$ στα σύνορα των ενδιάμεσων τμημάτων. Οι τιμές $P_0$ και $\epsilon_0$ προσδιορίζονται ανάλογα με την "+"\"κύρια\" καταστατική εξίσωση. "+
                            r"Συνεπώς, αρχίζοντας με τις τιμές $\rho_0$, $P_0$ και $\epsilon_0$ και ορίζοντας την τιμή του $\Gamma_1$, υπολογίζεται αρχικά η σταθερά $Κ_1$ και έπειτα οι συνοριακές τιμές $P_1$ και $\epsilon_1$, για το πρώτο πολυτροπικό τμήμα. Στη συνέχεια, γνωρίζοντας τις τιμές $\rho_1$, $P_1$ και $\epsilon_1$ και ορίζοντας την τιμή του $\Gamma$ υπολογίζονται, με την ίδια σειρά όπως πριν, "+
                            r"η σταθερά $Κ_2$ και οι συνοριακές τιμές  $P_2$ και $\epsilon_2$, για το δεύτερο πολυτροπικό τμήμα. Η διαδικασία επαναλάμβανεται αυτούσια και στα επόμενα πολυτροπικά τμήματα, μέχρι το τελευταίο $n$-οστό τμήμα και τον υπολογισμό των τιμών $K_n$, $P_n$ και $\epsilon_n$. Με το πέρας της διαδικασίας προκύπτει η συνολική καταστατική εξίσωση του πολυτροπικού στρώματος του πυρήνα. Η συνολική καταστατική εξίσωση του Αστέρα Νετρονίων δίνεται από τη σχέση:",
                            "sec1_text_poly4b": "με την καταστατική εξίσωση του **ΠΥΡΗΝΑ** να είναι τώρα:",
                            "sec1_text_poly4c": r"Επιπλέον, έχοντας διαθέσιμες $l$ επιλογές για τους δείκτες $\Gamma_i$ και ένα πλήθος $n$ πολυτροπικών τμημάτων, μπορεί κανείς να παράξει:",
                            "sec1_text_poly4d": "διαφορετικές καταστατικές εξισώσεις για το πολυτροπικό στρώμα (και κατ' επέκταση συνολικά για τον Αστέρα Νετρονίων), διαμορφώνοντας ένα **πλέγμα** εξισώσεων στον χώρο "+r"$P-\rho$, όπως θα διαπιστώσετε μόνοι σας παρακάτω.",
                            "sec1_gridpar_title": ">Επιλογή παραμέτρων του πολυτροπικού πλέγματος",
                            "sec1_Gamma_vals_select": "**>>Τιμές για τον δείκτη **"+r"$\Gamma$:",
                            "sec1_Gamma_vals_choice1": r"2 τιμές: {1,4}",
                            "sec1_Gamma_vals_choice2": r"4 τιμές: {1,2,3,4}",
                            "sec1_segments_select": "**>>Αριθμός πολυτροπικών τμημάτων** "+r"$n$:",
                            "sec1_final_dens_select": "**>>Τελική πυκνότητα μάζας** "+r"$\rho_ν$:",
                            "sec1_main_eos_select": "**>>\"Κύρια\" καταστατική εξίσωση**:",
                            "sec1_poly_grid_scan": "**>>Σκανάρισμα του πλέγματος**:",
                            "sec1_poly_grid_graph": ">Διάγραμμα πολυτροπικών πλεγμάτων",
                            "mass_density": "Πυκνότητα μάζας",
                        "section_2": "Η ΜΕΤΑΒΑΣΗ MAXWELL",


    },
    "widget_4": {       "title": "Widget 4: Σκανάρισμα περιοχής σταθερής \"παράξενης\" (strange) κουάρκ ύλης",
                        "subtitle": "Εκτός από τους Αστέρες Νετρονίων, διερευνάται και ένας άλλος τύπος συμπαγών αστέρων: οι Αστέρες Κουάρκ. Όπως αποκαλύπτει το όνομά τους, οι τελευταίοι αποτελούνται από περιορισμένη κουαρκιονική ύλη και στη συνήθη θεώρηση τους δεν περιλαμβάνουν εξωτερική κρούστα. Εμπίπτουν έτσι, στη γενική κατηγορία των Αυτοδεσμευμένων Αστέρων:",
                        "definition": "***Αυτοδεσμευμένοι Αστέρες***: Συμπαγείς διαμορφώσεις αστέρων με καταστατική εξίσωση όπου η ενεργειακή πυκνότητα έχει μη μηδενική τιμή σε πίεση μηδέν",
                        "subtitle_2": "Εάν η ύλη των παράξενων κουάρκ είναι αυτοδεσμευμένη, τότε οι σφαίρες που αποτελούνται από ύλη παράξενων κουάρκ δεσμεύονται λόγω της μηδενικής συνολικής πίεσης. Η βαρυτική έλξη δεν είναι απαραίτητη για την υδροστατική ισορροπία. Στην πραγματικότητα, η βαρύτητα καθορίζει μόνο ένα όριο στη μέγιστη μάζα της σφαίρας "+
                        "ύλης κουάρκ. Η ενεργειακή πυκνότητα στο εσωτερικό αυτών των δεσμευμένων σφαιρών ύλης παράξενων κουάρκ είναι σταθερή και προκύπτει από την ενεργειακή πυκνότητα του κενού. Επομένως, τα αυτοδεσμευμένα αστέρια παρουσιάζουν μια σχέση μάζας-ακτίνας μιας σφαίρας με σταθερή ενεργειακή πυκνότητα:",
                        "subtitle_3": "Οι εξισώσεις κατάστασης που περιγράφουν την ύλη των κουάρκ μέσα σε αστρικές διαμορφώσεις διαφέρουν από αυτές για την αδρονική ύλη. Παρακάτω, παρουσιάζουμε δύο τύπους εξισώσεων κατάστασης για τα αστέρια κουάρκ. Επιλέξτε έναν τύπο για να δείτε πληροφορίες σχετικά με αυτόν.",
                        "mit_model_btn": " MIT BAG μοντέλο",
                            "mit_model_title": "ΤΟ ΜΟΝΤΕΛΟ \"MIT BAG\"",
                        "cfl_model_btn": "CFL μοντέλο",
                            "cfl_model_title": "ΤΟ ΜΟΝΤΕΛΟ \"CFL\"",    
    }

    },
    "en": { "Default_widget_message": "⚙️ Please select a widget to experiment.",
            "core": "CORE",
            "layer": "CRUST LAYER",
        "widget_1": {   "title": "Widget 1: Describing the structure of a Neutron Star I",
                        "subtitle": "In the analysis, the Neutron Star is considered to be composed of two parts: the CRUST (externally) and the CORE (internally). Each part is described by its own equation of state.",
                        "section": "The CRUST",
                            "text": "The **crust** of a Neutron Star consists of **four layers**. Its equation of state is well-known and well-defined. Hover over the curve of a layer to see the formula of its equation of state and make its respective graph bolder, "+
                            "as well as highlight the region of the layer in the 2D illustration of the star.",
                            "graph1_title": ">Detailed Crust Equation of State: ε<sub>crust</sub>(P)",
                            "graph2_title": ">Schematic 2D illustration of the structure of a Neutron Star",
                            "message_title": "**>>Info**",
                            "message_region": "You are on the region: ",
                            "message_region_eos": "Equation of state: ",
                            "message_p_range": "Pressure P range: ",
                            "star_mass_slider": "**>>Mass of the Neutron Star**"+r" ($M_\odot$)"
        },
        "widget_2": {   "title": "Widget 2: Describing the structure of a Neutron Star II",
                        "subtitle": "In the analysis, the Neutron Star is considered to be composed of two parts: the CRUST (externally) and the CORE (internally). Each part is described by its own equation of state.",
                        "section": "THE CORE",
                            "text": "The **core** of a neutron star is also of particular interest. In the simplest case, the core is treated as a single layer and described by one constitutive equation. "+
                            "However, since the exact composition of the star's core remains unknown, its equation of state is also unknown. There are various theoretical models that attempt to highlight the correct formalism. "+
                            "Below, we present graphical representations for 21 \"main\" such models of equations of state. Select a model to see the corresponding fomrula of the equation of state and to see its graph in a separate diagram.",
                            "graph1_title": ">Models for Core Equation of State: ",
                            "graph1_memo": ">Memo",
                            "graph1_memo_text_caus": " no causality violation: ",
                            "graph1_memo_text_no_caus": " causality violation: ",
                            "graph1_memo_checklist": " (make bolder this part of the curves)",
                            "graph1_memo_text_eostype1": "**>>Type 1**",
                            "graph1_memo_text_eostype2": "**>>Type 2**",
                            "graph1_memo_text_genformula": "**General formula: **",
                            "graph1_memo_text_models": "**Models: **",
                            "model_select_title": ">Selection of a specific model for the Equation of State of the core:  ",
                            "model_select_choice": "**>>Model:  **",
                            "model_select_fullname": "**>>Fullname:  **",
                            "model_select_type": "**>>Type:  **",
                            "model_select_formula": "**>>Formula:  **",
                            "graph2_title": ">Graph of selected model: "
                        
    },
    "widget_3": {       "title": "Widget 3: Artificial generation of equations (polytropic and linear equations of state)",
                        "subtitle": "In the simplest case, where one of the 21 \"main\" models of constitutive equations is used for the core,  "+
                        "the total equation of state of the Neutron Star is given by the relation:",
                        "total_eos_form": r"""
                        $
                        \epsilon(P)=
                        \begin{cases}
                        \epsilon_{crust}(P), & P<P_{crust-core} \\
                        \epsilon_{main}(P), & P\geq P_{crust-core}
                        \end{cases}
                        $
                        """,
                        "subtitle_2": "where the core's equation of state is: ",
                        "core_eos_form_main": r"$\epsilon_{core}(P)=\epsilon_{main}(P)$",
                        "subtitle_3": r"""and the boundary pressure $P_{crust-core}$ is $0.696$ $MeV\cdot fm^{-3}$ for the ***PS*** equation of state and """+
                        r"""$0.184$ $MeV\cdot fm^{-3}$ for the rest "main" equations of state.""",
                        "section_1": "THE POLYTROPIC GRID",
                            "sec1_show_method_btn": "Show methodology",
                            "sec1_text_poly1": "Sometimes, the 21 \"main\" models for the constitutive equation of the core are not enough. Specifically, "+
                            r"some studies require (particularly) detailed and dense coverage and sampling of the $M-R$ and $\epsilon-P$ areas, which cannot be achieved using only the 21 "+ "\"main\" models. "+
                            "In such cases, various strategies can be applied to artificially generate a sufficiently large number of constitutive equations. In this *widget*, you can explore the methodology of **polytropic equations** and construct **polytropic grids**.",
                            "sec1_text_poly2": "The methodology of polytropic equations splits the **CORE** of the Neutron Star into two layers. The **first layer** extends into the pressure region: "+r"$P\in [P_{crust-cote},P_0]$ (or equivalently the mass density region: $\rho \in[\rho_{crust-core},\rho_0]$) and features one of the"+
                            "\"main\" models as equation of state. The **second layer** extends into the pressure region: "+ r"$P\in[P_0,P_n]$ (or equivalently the mass density region: $\rho \in[\rho_0,\rho_n]$). This layer is divided into $n$ polytropic segments, each of which features a dinstict polytropic relation between the pressure and the energy density. "+
                            "The total equation of state of the second layer is a piecewise function combining all these dinstict polytropic relations. "+r"The values of $P_0$ and $P_n$ (or equivalently $\rho_0$ and $\rho_n$) are arbitrarily selected. Typically, nuclear saturation density is chosen as the starting point: $\rho_0=\rho_{sat}$.",
                            "sec1_text_poly3a": r"In every polytropic segment $(\rho_{i-1}\leq\rho\leq\rho_i)$, we find the following relationship between pressure and energy density",
                            "sec1_text_poly3b": r"where the value of the constant $K_i$, is determined from the pressure and mass density at the previous fiducial point as follows",
                            "sec1_text_poly3c": r"and the polytropic index of the segment $\Gamma_i$, is given by",
                            "sec1_text_poly3d": r"The value of $\Gamma_i$ at each segment is usually arbitrarily chosen.  For $\Gamma_i\neq1$, the segments's relation between the pressure and the energy density reads",
                            "sec1_text_poly3e": r"while for $\Gamma_i=1$, the corresponding relation is",
                            "sec1_text_poly4a": r"The division into polytropic segments is done in such a way that the segments are of equal length in terms of the logarithm of density ($\log{\rho$}). The division yields the density values $\rho_i$ at the boundaries of the intermediate segments. The values $P_0$ and $\epsilon_0$ are determined according to the "+"\"main\" equation of state. "+
                            r"Therefore, starting with the values $\rho_0$, $P_0$ and $\epsilon_0$ and defining the value of $\Gamma_1$, we first calculate the constant $K_1$ and then the boundary values $P_1$ and $\epsilon_1$ for the first polytropic segment. Next, knowing the values $\rho_1$, $P_1$ and $\epsilon_1$ and defining the value of $\Gamma_2$, we calculate, in the same order as before, "+
                            r"the constant $K_2$ and the boundary values $P_2$ and $\epsilon_2$ for the second polytropic segment. The process is repeated in the same way for the subsequent polymodal sections, up to the last $n$-th segment and the calculation of the values $K_n$, $P_n$ and $\epsilon_n$. At the end of the process, the equation of state for the polytropic layer of the core is obtained. The total constitutive eqution of the Neutron Star reads:",
                            "sec1_text_poly4b": "with the constitutive equation of **CORE** now being:",
                            "sec1_text_poly4c": r"for a given number $l$ of possible choices for $\Gamma_i$ and a certain number of $n$ polytropic segments, one can produce:",
                            "sec1_text_poly4d": "different constitutive equations for the multimodal layer (and, by extension, for the neutron star as a whole), forming a **grid** of equations in" +r"$P-\rho$ space, as you will see for yourselves below.",
                            "sec1_gridpar_title": ">Polytropic grid parameter selection",
                            "sec1_Gamma_vals_select": "**>>**"+r"$\Gamma$"+"** values selection**:",
                            "sec1_Gamma_vals_choice1": r"2 values: {1,4}",
                            "sec1_Gamma_vals_choice2": r"4 values: {1,2,3,4}",
                            "sec1_segments_select": "**>>Number of polytropic segments** "+r"$n$:",
                            "sec1_final_dens_select": "**>>Final mass density** "+r"$\rho_ν$:",
                            "sec1_main_eos_select": "**>>\"Main\" equation of state**:",
                            "sec1_poly_grid_scan": "**>>Grid scanning**:",
                            "sec1_poly_grid_graph": ">Polytropic grid graph",
                            "mass_density": "Mass density",
                        "section_2": "THE MAXWELL TRANSITION",

    },
    "widget_4": {       "title": "Widget 4: Scanning the stability window of \"strange\" quark matter",
                        "subtitle": "In addition to Neutron Stars, another type of compact stars is under investigation: Quark Stars. As their name reveals, the latter consist of confined quarkyonic matter and in their usual considerations they do not include an outer crust. Hence, they fall under the general category of Selfbound Stars:",
                        "definition": "***Selfbound Stars***: Compact star configurations with an euqation of state where the energy density has nonvanishing value at zero pressure",
                        "subtitle_2": "If bulk strange quark matter is selfbound, then spheres comprising strange quark matter are bound by virtue of the vanishing total pressure. The gravitational attraction is not needed for hydrostatic equilibrium. In fact, gravity only defines a limit on the maximum mass of the quark matter sphere. The energy density in the interior of these bound spheres of strange quark matter is "+
                                    "constant, obtained by the vacuum energy density. Therefore, selfbound stars feature a mass-radius relationship of a sphere with fixed energy density:",
                        "subtitle_3": "The equations of state that describe quark matter inside stellar configurations differ from the ones for hadronic matter. Below, we present two types of equations of state for Quark Stars. Choose a type to see info about it.",            
                        "mit_model_btn": "MIT BAG model",
                            "mit_model_title": "ΤΗΕ \"MIT BAG\" MODEL",
                        "cfl_model_btn": "CFL model", 
                            "cfl_model_title": "THE \"CFL\" MODEL",   
    }                   
        
    }
}

# Language dictionary for the eos page
translations_tovpage = {
    "el": {
        "back_to_home": "Αρχική",
        "tov_title": "Επίλυση εξισώσεων TOV",
        "tov_intro": "Σε αυτή τη σελίδα μπορείτε να εξερευνήσετε την διαδικασία επίλυσης των εξισώσεων TOV για συμπαγείς αστέρες."
    },
    "en": {
        "back_to_home": "Home",
        "tov_title": "Solving TOV equations",
        "tov_intro": "On this page, you can explore the process of solving TOV equations for compact stars."
    }
}