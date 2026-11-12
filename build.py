#!/usr/bin/env python3
"""Static site generator for diamantiskaranastasis.com (EL + EN)."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
E = html.escape

SOCIAL = [
    ("Instagram", "https://www.instagram.com/diamond_karanastasis/"),
    ("Facebook", "https://www.facebook.com/diamantis.karanastasis/"),
    ("YouTube", "https://www.youtube.com/channel/UCJ98Gt_ZgGxIDcLVIK1UcEQ"),
    ("Vimeo", "https://vimeo.com/user14352981"),
    ("LinkedIn", "https://www.linkedin.com/in/diamantis-karanastasis-67392116/"),
    ("X / Twitter", "https://twitter.com/diamantis_kar"),
    ("IMDb", "https://www.imdb.com/name/nm1007350/"),
]
SITES = [("dacos.gr", "https://dacos.gr"), ("birigogo.gr", "https://birigogo.gr"), ("mybloodthemovie.com", "https://mybloodthemovie.com")]
MAIL = "info@diamantiskaranastasis.com"

L = {
 "el": dict(
   lang="el", other="en", other_label="EN",
   name_first="Διαμαντής", name_last="Καραναστάσης",
   roles="Ηθοποιός / Σκηνοθέτης / Παραγωγός / Voice-Over Artist",
   desc="Ο Διαμαντής Καραναστάσης είναι ηθοποιός σε θέατρο και τηλεόραση, σκηνοθέτης, βραβευμένος κινηματογραφιστής & διακεκριμένος voice-over artist.",
   nav=[("", "Αρχική"), ("biografiko/", "Βιογραφικό"), ("theatro/", "Θέατρο"), ("tileorasi/", "Τηλεόραση"), ("kinimatografos/", "Σινεμά"), ("epikoinonia/", "Επικοινωνία")],
   paths=dict(home="", bio="biografiko/", theatre="theatro/", tv="tileorasi/", cinema="kinimatografos/", contact="epikoinonia/"),
   words_h="Λίγα λόγια",
   words="Γεννήθηκα στη Λάρισα το 1974. Εκεί μεγάλωσα μέχρι τα 18 μου. Το 1992 πέρασα στο Πολυτεχνείο και ήρθα στην Αθήνα να σπουδάσω στο τμήμα Ηλεκτρολόγων Μηχανικών και Μηχανικών Ηλεκτρονικών Υπολογιστών. Κατά τη διάρκεια των σπουδών μου άρχισα να ψάχνω τρόπους να κυνηγήσω το όνειρό μου και ξεκίνησα τη θεατρική μου εκπαίδευση…",
   words_more="Η πορεία μου",
   career_h="Θέατρο, Τηλεόραση, Σινεμά, Voice-Overs",
   tiles=[("theatre", "Θέατρο", "tile-theatre"), ("tv", "Τηλεόραση", "tile-tv"), ("cinema", "Σινεμά", "tile-cinema"), ("voice", "Voice-Overs", "tile-voice")],
   voice_note="10.000+ εκφωνήσεις",
   photos_h="Στιγμές",
   contact_h="Επικοινωνήστε μαζί μου",
   contact_p="Επικοινωνήστε μαζί μου στο",
   sites_h="Sites", social_h="Social",
   rights="Διαμαντής Καραναστάσης",
 ),
 "en": dict(
   lang="en", other="el", other_label="ΕΛ",
   name_first="Diamantis", name_last="Karanastasis",
   roles="Actor / Director / Producer / Voice-Over Artist",
   desc="Diamantis Karanastasis is a theatre and television actor, director, award-winning filmmaker and distinguished voice-over artist.",
   nav=[("en/", "Home"), ("en/biography/", "Biography"), ("en/theatre/", "Theatre"), ("en/television/", "Television"), ("en/cinema/", "Cinema"), ("en/contact/", "Contact")],
   paths=dict(home="en/", bio="en/biography/", theatre="en/theatre/", tv="en/television/", cinema="en/cinema/", contact="en/contact/"),
   words_h="My words",
   words="I was born in Larissa, Greece. I studied Computer Engineering at the National Polytechnic University of Athens. During my studies there, I followed my passion and started my drama education.",
   words_more="My full path",
   career_h="Theatre, TV, Cinema, Voice-Overs",
   tiles=[("theatre", "Theatre", "tile-theatre"), ("tv", "Television", "tile-tv"), ("cinema", "Cinema", "tile-cinema"), ("voice", "Voice-Overs", "tile-voice")],
   voice_note="10,000+ voice-overs",
   photos_h="Moments",
   contact_h="Get in touch",
   contact_p="Contact me at",
   sites_h="Sites", social_h="Social",
   rights="Diamantis Karanastasis",
 ),
}

# ---------------------------------------------------------------- page bodies
def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)

def ul(items, cls="credits"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'

PAGES = {
 "el": {
  "bio": dict(title="Βιογραφικό", img="bio", q="«Η τέχνη είναι ένα ψέμα που μας βοηθάει να ανακαλύψουμε την αλήθεια»", qa="Πάμπλο Πικάσο",
   body=p(
    "Γεννήθηκα στη Λάρισα το 1974. Εκεί μεγάλωσα μέχρι τα 18 μου. Το 1992 πέρασα στο Πολυτεχνείο και ήρθα στην Αθήνα να σπουδάσω στο τμήμα Ηλεκτρολόγων Μηχανικών και Μηχανικών Ηλεκτρονικών Υπολογιστών. Κατά τη διάρκεια των σπουδών μου άρχισα να ψάχνω τρόπους να κυνηγήσω το όνειρό μου και ξεκίνησα τη θεατρική μου εκπαίδευση λίγα χρόνια μετά, στη σχολή του Βασίλη Διαμαντόπουλου.",
    "Στη σχολή ακόμη, μου πρότειναν την πρώτη μου δουλειά, έναν πρωταγωνιστικό ρόλο σε μια σειρά που ετοίμαζε τότε ο Νίκος Κουτελιδάκης σε σενάριο Ελένης Ζιώγα, με τίτλο «Σαν Αδελφές» για την ΕΡΤ. Από τότε ξεκίνησα να δουλεύω μόνιμα στο <a href=\"/theatro/\">θέατρο</a> και την <a href=\"/tileorasi/\">τηλεόραση</a>, με μόνιμο σύμβουλο στις επιλογές μου το ένστικτό μου και μοναδικό κριτήριό μου, την παιδική αγάπη για τη δουλειά μου.",
    "Έχω πρωταγωνιστήσει σε πολλές θεατρικές παραστάσεις και γνωστές τηλεοπτικές σειρές. Έχω αναλάβει την παραγωγή σε πολλές θεατρικές παραστάσεις.",
    "Με τη <a href=\"https://dacos.gr\">φωνή</a> μου έχω επενδύσει πάνω από 10.000 τηλεοπτικές και ραδιοφωνικές διαφημίσεις αλλά και ντοκιμαντέρ, τηλεοπτικές εκπομπές και επιλεγμένες ταινίες animation (Madagascar, Ice Age, Star Wars: Clone Wars κ.α.).",
    "Με το ιδιόκτητο post-production studio μου <a href=\"https://dacos.gr\">DACOS</a>, έχω αναλάβει εκατοντάδες οπτικοακουστικές παραγωγές και κινηματογραφήσεις.",
    "Η πρώτη μου σκηνοθεσία σε μεγάλου μήκους ταινία είναι το <a href=\"/kinimatografos/\">ΑΙΜΑ</a> (αγγλ. «<a href=\"https://mybloodthemovie.com\">My Blood</a>») όπου ανέλαβα και την παραγωγή, το σενάριο, το μοντάζ και έπαιξα έναν από τους δύο βασικούς ανδρικούς ρόλους. Η ταινία είναι μια εντελώς ανεξάρτητη παραγωγή που κατάφερε χωρίς καμία φεστιβαλική προώθηση και υποστήριξη να έχει δυο υποψηφιότητες στην Ελληνική Ακαδημία Κινηματογράφου κερδίζοντας το ένα βραβείο αλλά και 9 συνολικά βραβεία και πολλές υποψηφιότητες και διακρίσεις σε Κινηματογραφικά Φεστιβάλ σε όλο τον κόσμο. Ένα μικρό θαύμα, που με κάνει πολύ περήφανο.",
    "Πιο πρόσφατα ανέλαβα την σκηνοθεσία, την κινηματογράφηση αλλά και όλο το post production, του έργου «ΠΥΡΑΜΙΔΕΣ» (κειμ. Ανδρέα Φλουράκη) για το Θέατρο Τέχνης Καρόλου Κουν, λαμβάνοντας εξαιρετικές κριτικές. Το έργο δημιουργήθηκε αποκλειστικά για το διαδίκτυο σε συνθήκες καραντίνας και κινηματογραφήθηκε σε όλους τους χώρους του ιστορικού θεάτρου, προβάλλοντας την απουσία του κοινού, την ερημιά του χώρου και τη μοναξιά του καλλιτέχνη.",
    "Η ταινία μου «11 μ.μ.» τον Απρίλιο του 2021, με πρωταγωνιστές την Αθήνα, τους άδειους δρόμους της και τους κλειστούς χώρους πολιτισμού, κατά τη διάρκεια της δεύτερης καραντίνας, είχε πολύ σημαντική απήχηση εντός Ελλάδας και έχει ξεκινήσει ήδη το ταξίδι της σε φεστιβάλ.")
    + '<blockquote class="endq">«Η αφετηρία και η βάση του θεάτρου, όπως και κάθε μορφής τέχνης, είναι η ποίηση και η μαγεία»<cite>Κάρολος Κουν</cite></blockquote>'),
  "theatre": dict(title="Θέατρο", img="theatre", q="«Η αφετηρία και η βάση του θεάτρου, όπως και κάθε μορφής τέχνης, είναι η ποίηση και η μαγεία»", qa="Κάρολος Κουν",
   body='<h2 class="sub">Σημαντικές παραστάσεις</h2>' + ul([
    "<b>«Τρεις Αδελφές»</b> του Αντόν Τσέχωφ<span>Θέατρο Τέχνης, 2008 · Σκηνοθεσία Μαριάννα Κάλμπαρη</span>",
    "<b>«Love, Love, Love»</b> του Μάικ Μπάρτλετ<span>Θέατρο Τέχνης, 2012 · Σκηνοθεσία Μαριάννα Κάλμπαρη</span>",
    "<b>«Τα Κόκκινα Φανάρια»</b> του Αλέκου Γαλανού (διασκευή Νίκου Μαστοράκη)<span>Δημοτικό Θέατρο Πειραιά, 2014 · Σκηνοθεσία Νίκος Μαστοράκης</span>",
    "<b>«Το Τρελό Αίμα»</b> του Παντελή Πρεβελάκη (σύνθεση Άντζελα Μπρούσκου)<span>Θέατρο Τέχνης, 2015 · Σκηνοθεσία Άντζελα Μπρούσκου</span>",
    "<b>«Φόβος»</b> του Στέφαν Τσβάιχ<span>Δημοτικό Θέατρο Καλαμάτας, 2016 · Σκηνοθεσία Έλενα Πέγκα</span>",
    "<b>«Ιστορία Έρωτα και Αναρχίας»</b> της Λίνα Βερτμίλερ<span>BIOS, 2019 · Σκηνοθεσία Γιάννης Λασπιάς</span>",
    "<b>«Ελευθερία στη Βρέμη»</b> του Ράινερ Βέρνερ Φασμπίντερ<span>Θέατρο Τέχνης &amp; ΔΗΠΕΘΕ Κρήτης, 2022–2023 · Σκηνοθεσία Νίκος Μαστοράκης</span>",
   ]) + "GALLERY_THEATRE"),
  "tv": dict(title="Τηλεόραση", img="tv", q="«Η τηλεόραση είναι πιο κοντά στην πραγματικότητα από ό,τι τα βιβλία. Η τρέλα της τηλεόρασης είναι η τρέλα της ανθρώπινης ζωής»", qa="Καμίλ Πάλια",
   body='<h2 class="sub">Τηλεοπτικές δουλειές</h2>' + ul([
    "<b>«So Long, Marianne»</b><span>2024 · ρόλος Nick Katsikas · 7 επεισόδια · NRK (Νορβηγία)</span>",
    "<b>«Στοργή»</b><span>2023 · ρόλος Γιώργης · 3 επεισόδια · ΣΚΑΪ</span>",
    "<b>«Γιούγκερμαν»</b><span>2007–2008 · ρόλος Μιχάλης Καραμάνος · 9 επεισόδια · σκην. Γρηγόρης Καραντινάκης · ΑΝΤ1</span>",
    "<b>«7 Θανάσιμες πεθερές»</b><span>2007 · ρόλος Αντώνης · 3 επεισόδια · σκην. Γρηγόρης Πετρινιώτης · MEGA</span>",
    "<b>«Ιστορίες του αστυνόμου Μπέκα»</b><span>2006 · ρόλος Φαίδων Κάψης · 2 επεισόδια · σκην. Νίκος Κρητικός · ALPHA</span>",
    "<b>«Δείξε μου το φίλο σου»</b><span>2005–2006 · ρόλος Γιώργος · 20 επεισόδια · σκην. Άκης Σταματιάδης · ΑΝΤ1</span>",
    "<b>«Κρυφά μονοπάτια»</b><span>2005–2006 · σκην. Μανούσος Μανουσάκης · ΑΝΤ1</span>",
    "<b>«Για πάντα μαζί»</b><span>2005 · τηλεταινία</span>",
    "<b>«Με θέα στο πέλαγο»</b><span>2004 · ρόλος Στράτος Πολίτης · 21 επεισόδια · σκην. Γιάννης Βασιλειάδης · MEGA</span>",
    "<b>«Αμαρτίες Γονέων»</b><span>2003–2004 · ρόλος Ανδρέας · 29 επεισόδια · σκην. Σίσσυ Σμυριλιού · MEGA</span>",
    "<b>«Η αγάπη ήρθε από μακριά»</b><span>2002 · ρόλος Σπύρος Βραχνός · σκην. Μανούσος Μανουσάκης · ΑΝΤ1</span>",
    "<b>«Λίφτινγκ»</b><span>2001–2002 · ρόλος Μίλτος · 36 επεισόδια · σκην. Γρηγόρης Πετρινιώτης · ΑΝΤ1</span>",
    "<b>«Αθώος ή Ένοχος»</b><span>2000–2001 · ρόλος Θωμάς · 11 επεισόδια · σκην. Γρηγόρης Καραντινάκης · ΑΝΤ1</span>",
    "<b>«Κωνσταντίνου και Ελένης»</b><span>2000 · ρόλος Δρ Στέλιος Μαρκίδης · 1 επεισόδιο · σκην. Κώστας Λυχναράς</span>",
    "<b>«Σαν Αδελφές»</b><span>1999 · σκην. Νίκος Κουτελιδάκης · ΕΡΤ</span>",
   ]) + p("Περισσότερα στη σελίδα μου στο " + ext("https://www.imdb.com/name/nm1007350/", "IMDb") + ".")),
  "cinema": dict(title="Σινεμά", img="cinema", q="«Το βασικό γνώρισμα του μεγάλου ηθοποιού είναι ότι του αρέσει πολύ ο εαυτός του όταν παίζει ένα ρόλο»", qa="Τσάρλι Τσάπλιν",
   body=p("Έχω παίξει, σκηνοθετήσει και παραγάγει ταινίες μεγάλου και μικρού μήκους. Μεταξύ άλλων, πρωταγωνίστησα στις «" + ext("https://www.imdb.com/title/tt8220786/", "Ιστορίες χωρίς χρόνο") + "» (2017) του Βασίλη Ραΐση, που κέρδισαν το Βραβείο Κοινού στο 58ο Διεθνές Φεστιβάλ Κινηματογράφου Θεσσαλονίκης. Στη βιογραφική ταινία «Υπάρχω» (2024) του Γιώργου Τσεμπερόπουλου υποδύθηκα τον Μανώλη Χιώτη, κορυφαία μορφή της λαϊκής μουσικής και συνεργάτη του Στέλιου Καζαντζίδη, σε μια ταινία που έγινε μία από τις εμπορικότερες ελληνικές ταινίες όλων των εποχών.",
    "Η πρώτη μου ταινία μεγάλου μήκους ως σκηνοθέτης, το <b>ΑΙΜΑ</b> (" + ext("https://mybloodthemovie.com", "My Blood") + ", 2011), που έγραψα, παρήγαγα, μόνταρα και στην οποία πρωταγωνίστησα, είναι μια ανεξάρτητη, no-budget παραβολή πάνω στον μύθο του Οιδίποδα. Προβλήθηκε σε φεστιβάλ σε ΗΠΑ, Ηνωμένο Βασίλειο, Ινδονησία, Ινδία, Κροατία, Ισπανία και Ολλανδία, κέρδισε εννέα διεθνή βραβεία και, στα Βραβεία της Ελληνικής Ακαδημίας Κινηματογράφου, μία υποψηφιότητα και ένα βραβείο.")
   + '<h2 class="sub">ΑΙΜΑ: βραβεία και διακρίσεις</h2>' + ul([
    "Βραβείο Επιτροπής, Special Jury Prize – World Cinema Dramatic<span>Amsterdam Film Festival 2012 (Ολλανδία)</span>",
    "Βραβείο Καλύτερης Πρωτότυπης Μουσικής (Σταύρος Γασπαράτος)<span>Ελληνική Ακαδημία Κινηματογράφου 2013</span>",
    "Υποψηφιότητα Α’ Γυναικείου Ρόλου (Βίκυ Βολιώτη)<span>Ελληνική Ακαδημία Κινηματογράφου 2013</span>",
    "Best Concept for Fiction Film<span>London Greek Film Festival 2013</span>",
    "Best Actress (Βίκυ Βολιώτη)<span>London Greek Film Festival 2013</span>",
    "Best Screenplay<span>London Greek Film Festival 2013</span>",
    "Special Festival Mention<span>Noida International Film Festival 2014 (Ινδία)</span>",
    "Honorable Mention<span>Indie Gathering International Film Festival 2014 (Η.Π.Α.)</span>",
    "Gold Award<span>International Movie Awards (Ινδονησία)</span>",
    "Award of Recognition – Feature Film<span>The indieFEST 2018, La Jolla (Η.Π.Α.)</span>",
    "Υποψηφιότητες: Best Foreign Language Feature Film / Best Original Score / Best Original Screenplay / Best Editing<span>International Filmmaker Festival of World Cinema, London 2016</span>",
   ], "credits awards") + '<h2 class="sub">Άλλες συμμετοχές σε φεστιβάλ</h2>' + ul([
    "Επίσημη συμμετοχή<span>Gijón International Film Festival 2012 (Ισπανία)</span>",
    "Επίσημη συμμετοχή<span>Διεθνές Φεστιβάλ Κινηματογράφου της Αθήνας – Νύχτες Πρεμιέρας 2012</span>",
    "Επίσημη συμμετοχή<span>San Francisco Greek Film Festival 2013 (Η.Π.Α.)</span>",
    "Επίσημη συμμετοχή<span>Vukovar Film Festival 2013 (Κροατία)</span>",
    "Επίσημη συμμετοχή<span>Columbia Gorge International Film Festival 2014 (Η.Π.Α.)</span>",
   ]) + p("Το 2021, στην καραντίνα, σκηνοθέτησα τις «Πυραμίδες» του Ανδρέα Φλουράκη για το Θέατρο Τέχνης Καρόλου Κουν, την πρώτη πλήρως ψηφιακή ελληνική θεατρική παραγωγή για online κοινό. Ο κριτικός Δρ Κωνσταντίνος Μπούρας, στο Βήμα, πρότεινε ειδικό βραβείο για την κινηματογράφηση και το μοντάζ.",
    "Η ταινία μου «11 μ.μ.» τον Απρίλιο του 2021, με πρωταγωνιστές την Αθήνα, τους άδειους δρόμους της και τους κλειστούς χώρους πολιτισμού, κατά τη διάρκεια της δεύτερης καραντίνας, είχε πολύ σημαντική απήχηση εντός Ελλάδας και έχει ξεκινήσει ήδη το ταξίδι της σε φεστιβάλ.")),
 },
 "en": {
  "bio": dict(title="Biography", img="bio", q="«Art is a lie that makes us realize truth, at least the truth that is given us to understand.»", qa="Pablo Picasso",
   body=p("I was born in Larissa, Greece. I studied Computer Engineering at the National Polytechnic University of Athens. During my studies there, I followed my passion and started my drama education.",
    "I work in <a href=\"/en/theatre/\">Theatre</a>, <a href=\"/en/television/\">TV</a> and <a href=\"/en/cinema/\">Cinema</a> since 1998 and performed in critically acclaimed stage productions and popular Greek TV series.",
    "My first feature film direction <a href=\"https://mybloodthemovie.com\">“My Blood”</a> (also produced, screenplay writing and editing) achieved a total of 9 awards and multiple honours at festivals worldwide, including one nomination and one award at Greek Film Academy Awards.",
    "My <a href=\"https://dacos.gr\">voice</a> has been featured in over 10,000 advertisements, for Greek and International companies as well as in documentaries, narrations and Greek adaptations of blockbuster animation films.",
    "In my own post production studio <a href=\"https://dacos.gr\">DACOS</a> I have created hundreds of multimedia productions, video art and promotional videos and audios.")
    + '<blockquote class="endq">«The starting point and basis of theatre, as in every art form, is poetry and magic.»<cite>Karolos Koun</cite></blockquote>'),
  "theatre": dict(title="Theatre", img="theatre", q="«The starting point and basis of theatre, as in every art form, is poetry and magic.»", qa="Karolos Koun",
   body='<h2 class="sub">Notable theatre work</h2>' + ul([
    "<b>Anton Chekhov’s “Three Sisters”</b><span>Greek Art Theatre, Athens · Director Marianna Calbari</span>",
    "<b>Mike Bartlett’s “Love Love Love”</b><span>Greek Art Theatre, Athens · Director Marianna Calbari</span>",
    "<b>Alecos Galanos’ “Red Lights”</b> (Nikos Mastorakis’ adaptation)<span>Piraeus Municipal Theatre · Director Nikos Mastorakis</span>",
    "<b>P. Prevelakis’ “Crazy Blood”</b> (Angela Brouskou synthesis)<span>Greek Art Theatre, Athens · Director Angela Brouskou</span>",
    "<b>Stefan Zweig’s “Fear”</b><span>Kalamata – Thessaloniki – Kavala – Athens · Director Elena Penga</span>",
    "<b>Lina Wertmüller’s “Love and Anarchy”</b><span>BIOS, Athens · Director Giannis Laspias</span>",
    "<b>Rainer Werner Fassbinder’s “Bremen Freedom”</b><span>Greek Art Theatre &amp; Municipal Regional Theatre of Crete, 2022–2023 · Director Nikos Mastorakis</span>",
   ]) + "GALLERY_THEATRE"),
  "tv": dict(title="Television", img="tv", q="«Television is actually closer to reality than anything in books. The madness of TV is the madness of human life»", qa="Camille Paglia",
   body='<h2 class="sub">TV work</h2>' + ul([
    "<b>“So Long, Marianne”</b><span>2024 · as Nick Katsikas · 7 episodes · NRK (Norway)</span>",
    "<b>“Storgi”</b> (“Affection”)<span>2023 · as Giorgis · 3 episodes · SKAI</span>",
    "<b>“Yungermann”</b> (after the novel by M. Karagatsis)<span>2007–2008 · as Mihalis Karamanos · 9 episodes · director G. Karantinakis · ANT1</span>",
    "<b>“Epta thanasimes petheres”</b> (“Seven Deadly Mothers-in-law”)<span>2007 · as Antonis · 3 episodes · director G. Petriniotis · MEGA</span>",
    "<b>“Oi istories tou astynomou Beka”</b> (“Inspector Bekas’ Stories”)<span>2006 · as Faidon Kapsis · 2 episodes · director N. Kritikos · ALPHA</span>",
    "<b>“Deixe mou to filo sou”</b> (“Show Me Your Friend”)<span>2005–2006 · as Giorgos · 20 episodes · director A. Stamatiadis · ANT1</span>",
    "<b>“Kryfa monopatia”</b> (“Secret Paths”)<span>2005–2006 · director M. Manousakis · ANT1</span>",
    "<b>“Gia panta mazi”</b> (“Together Forever”)<span>2005 · TV movie</span>",
    "<b>“Me thea sto pelago”</b> (“View to the Sea”)<span>2004 · as Stratos Politis · 21 episodes · director Y. Vasiliadis · MEGA</span>",
    "<b>“Amarties goneon”</b> (“Sins of the Parents”)<span>2003–2004 · as Andreas · 29 episodes · director S. Smyriliou · MEGA</span>",
    "<b>“I agapi irthe apo makria”</b> (“Love Came from Afar”)<span>2002 · as Spyros Vrahnos · director M. Manousakis · ANT1</span>",
    "<b>“Lifting”</b><span>2001–2002 · as Miltos · 36 episodes · director G. Petriniotis · ANT1</span>",
    "<b>“Athoos i enohos”</b> (“Innocent or Guilty”)<span>2000–2001 · as Thomas · 11 episodes · director G. Karantinakis · ANT1</span>",
    "<b>“Constantine’s and Helen’s”</b><span>2000 · as Dr. Stelios Markidis · 1 episode · director K. Lychnaras</span>",
    "<b>“San adelfes”</b> (“Like Sisters”)<span>1999 · director N. Koutelidakis · ERT</span>",
   ]) + p("More info at my " + ext("https://www.imdb.com/name/nm1007350/", "IMDb page") + ".")),
  "cinema": dict(title="Cinema", img="cinema", q="«The basic essential of a great actor is that he loves himself in acting»", qa="Charlie Chaplin",
   body=p("I have acted in, directed and produced both feature and short films. Among others, I played the lead in Vassilis Raisis’ “" + ext("https://www.imdb.com/title/tt8220786/", "Timeless Stories") + "” (2017), winner of the Audience Award at the 58th Thessaloniki International Film Festival. In Giorgos Tsemberopoulos’ biographical film “Stelios” (2024) I portrayed Manolis Chiotis, a major figure in Greek folk music and partner of Stelios Kazantzidis, in a film that became one of the highest-grossing Greek films of all time.",
    "My debut feature as director, “" + ext("https://mybloodthemovie.com", "My Blood") + "” (“Aima”, 2011), which I also wrote, produced, edited and starred in, is an independent, no-budget parable based on the Oedipus myth. It screened at festivals in the United States, the United Kingdom, Indonesia, India, Croatia, Spain and the Netherlands, winning nine international awards, and received a nomination and a win at the Hellenic Film Academy Awards.")
   + '<h2 class="sub">My Blood: awards and honours</h2>' + ul([
    "Winner, Special Jury Prize – World Cinema Dramatic<span>Amsterdam Film Festival 2012</span>",
    "Winner, Best Original Music Score<span>Greek Film Academy Awards 2013</span>",
    "Nominated, Best Actress in a Leading Role<span>Greek Film Academy Awards 2013</span>",
    "Winner, Best Concept Fiction Feature<span>London Greek Film Festival</span>",
    "Winner, Best Actress (Vicky Volioti)<span>London Greek Film Festival</span>",
    "Winner, Best Screenplay (Diamantis Karanastasis)<span>London Greek Film Festival</span>",
    "Winner, Special Festival Mention<span>Noida International Film Festival</span>",
    "Winner, Festival Mention<span>Indie Gathering International Film Festival 2014 (USA)</span>",
    "Winner, Gold Award<span>International Movie Awards (Indonesia 2014)</span>",
    "Winner, Award of Recognition – Feature Film<span>The indieFEST (Aug 2018, La Jolla, USA)</span>",
    "Nominated for 4 awards: Best Foreign Language Feature Film, Best Original Score, Best Original Screenplay of a Foreign Language Film, Best Editing of a Foreign Language Film<span>International Filmmaker Festival of World Cinema (London 2016)</span>",
   ], "credits awards") + '<h2 class="sub">Official selections</h2>' + ul([
    "Official Selection<span>Gijón International Film Festival 2012</span>",
    "Official Selection<span>Athens International Film Festival 2012</span>",
    "Official Selection<span>San Francisco Greek Film Festival 2013</span>",
    "Official Selection<span>Vukovar Film Festival 2013</span>",
   ]) + p("During the 2021 lockdown I directed “Pyramides” (“Pyramids”) by Andreas Flourakis for the Karolos Koun Art Theatre, the first fully digital Greek theatre production made for online audiences. Critic Dr. Konstantinos Bouras, writing in To Vima, proposed a special award for its cinematography and editing.",
    "More info at my " + ext("https://www.imdb.com/name/nm1007350/", "IMDb page") + ".")),
 },
}

GALLERY_THEATRE = {
 "el": [("p-trelo-aima", "Το Τρελό Αίμα"), ("p-love", "Love, Love, Love"), ("p-anarchia", "Ιστορία Έρωτα και Αναρχίας"), ("p-fovos", "Φόβος")],
 "en": [("p-trelo-aima", "Crazy Blood"), ("p-love", "Love Love Love"), ("p-anarchia", "Love and Anarchy"), ("p-fovos", "Fear")],
}
MOMENTS = ["01","02","03","04","05","06","07","08","09","10","11","13","12","14","16"]
from PIL import Image as _Im
MSIZE = {g: _Im.open(os.path.join(OUT, "img", "m", f"t{g}.jpg")).size for g in MOMENTS}

CONTACT = {
 "el": dict(title="Επικοινωνία", img="contact", h="Αφήστε το μήνυμά σας"),
 "en": dict(title="Contact", img="contact", h="Leave your message"),
}

# ---------------------------------------------------------------- shell
def counterpart(lang, key):
    return "/" + L[L[lang]["other"]]["paths"][key]

def shell(lang, key, title, body, dark_header=True):
    t = L[lang]
    full_title = f"{title} | {t['name_first']} {t['name_last']}" if key != "home" else f"{t['name_first']} {t['name_last']} — {t['roles']}"
    nav = "".join(
        f'<a href="/{href}"{" aria-current=\"page\"" if href == t["paths"][key] else ""}>{E(lbl)}</a>' for href, lbl in t["nav"])
    alt_lang = L[lang]["other"]
    social = "".join(f'<li>{ext(u, E(n))}</li>' for n, u in SOCIAL)
    sites = "".join(f'<li>{ext(u, E(n))}</li>' for n, u in SITES)
    canon = "https://diamantiskaranastasis.com/" + t["paths"][key]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(t['desc'])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="{lang}" href="{canon}">
<link rel="alternate" hreflang="{alt_lang}" href="https://diamantiskaranastasis.com{counterpart(lang, key)}">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(t['desc'])}">
<meta property="og:image" content="https://diamantiskaranastasis.com/img/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,300..800;1,62..125,300..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body class="page-{key}">
<a class="skip" href="#main">{'Μετάβαση στο περιεχόμενο' if lang=='el' else 'Skip to content'}</a>
<header class="top">
  <a class="mark" href="/{t['paths']['home']}"><span>{E(t['name_first'])}</span> <b>{E(t['name_last'])}</b></a>
  <button class="burger" aria-expanded="false" aria-controls="nav" aria-label="Menu"><i></i><i></i></button>
  <nav id="nav">{nav}<a class="lang" href="{counterpart(lang, key)}" hreflang="{alt_lang}" lang="{alt_lang}">{t['other_label']}</a></nav>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="foot-grid">
    <div><h3>{E(t['contact_h'])}</h3><a class="mail" href="mailto:{MAIL}">{MAIL}</a></div>
    <div><h3>{t['sites_h']}</h3><ul>{sites}</ul></div>
    <div><h3>{t['social_h']}</h3><ul>{social}</ul></div>
  </div>
  <p class="legal">© <span id="yr">2026</span> {E(t['rights'])}</p>
</footer>
<script>
document.getElementById('yr').textContent=new Date().getFullYear();
const b=document.querySelector('.burger'),n=document.getElementById('nav');
b.addEventListener('click',()=>{{const o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',!o);document.body.classList.toggle('nav-open',!o);}});
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}}),{{rootMargin:'0px 0px -8% 0px'}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

const st=document.querySelector('.strip');
let touched=false;
if(st){{
 const step=()=>Math.max(st.clientWidth*0.8,280);
 document.querySelector('.slider .prev').onclick=()=>{{touched=true;st.scrollBy({{left:-step(),behavior:'smooth'}});}};
 document.querySelector('.slider .next').onclick=()=>{{touched=true;st.scrollBy({{left:step(),behavior:'smooth'}});}};
 const upd=()=>{{document.querySelector('.slider .prev').disabled=st.scrollLeft<5;document.querySelector('.slider .next').disabled=st.scrollLeft+st.clientWidth>=st.scrollWidth-5;}};
 st.addEventListener('scroll',upd,{{passive:true}});window.addEventListener('resize',upd);['pointerdown','wheel','touchstart','keydown'].forEach(ev=>st.addEventListener(ev,()=>touched=true,{{passive:true}}));st.querySelectorAll('img').forEach(i=>i.addEventListener('load',()=>{{if(!touched)st.scrollLeft=0;upd();}}));window.addEventListener('load',()=>{{st.scrollLeft=0;upd();}});st.scrollLeft=0;upd();
 const shots=[...st.querySelectorAll('.shot')],lb=document.querySelector('.lb'),li=lb.querySelector('img'),lc=lb.querySelector('.lb-c');let cur=0,x0=null;
 const show=i=>{{cur=(i+shots.length)%shots.length;li.src=shots[cur].dataset.full;lc.textContent=(cur+1)+' / '+shots.length;}};
 const open=i=>{{show(i);lb.hidden=false;document.body.style.overflow='hidden';lb.querySelector('.lb-x').focus();}};
 const close=()=>{{lb.hidden=true;document.body.style.overflow='';shots[cur].focus();}};
 shots.forEach((b,i)=>b.onclick=()=>open(i));
 lb.querySelector('.lb-x').onclick=close;lb.querySelector('.lb-p').onclick=e=>{{e.stopPropagation();show(cur-1)}};lb.querySelector('.lb-n').onclick=e=>{{e.stopPropagation();show(cur+1)}};
 lb.onclick=e=>{{if(e.target===lb)close();}};
 document.addEventListener('keydown',e=>{{if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1);}});
 lb.addEventListener('touchstart',e=>{{x0=e.touches[0].clientX}},{{passive:true}});
 lb.addEventListener('touchend',e=>{{if(x0===null)return;const d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>50)show(cur+(d<0?1:-1));x0=null;}});
}}
</script>
</body>
</html>
"""

def home(lang):
    t = L[lang]
    tiles = ""
    for i, (k, lbl, img) in enumerate(t["tiles"]):
        href = "https://dacos.gr" if k == "voice" else "/" + t["paths"][k]
        note = f'<small>{E(t["voice_note"])}</small>' if k == "voice" else ""
        tiles += f'<a class="tile reveal" href="{href}"><img src="/img/{img}.jpg" alt="" loading="lazy"><span class="n">0{i+1}</span><span class="l">{E(lbl)}{note}</span></a>'
    moments = "".join(f'<button class="shot" data-i="{n}" data-full="/img/m/{g}.jpg" aria-label="{E(t["photos_h"])} {n+1}"><img src="/img/m/t{g}.jpg" width="{MSIZE[g][0]}" height="{MSIZE[g][1]}" alt="" loading="lazy"></button>' for n, g in enumerate(MOMENTS))
    return f"""
<section class="hero">
  <img class="hero-img" src="/img/hero.jpg" alt="{E(t['name_first'])} {E(t['name_last'])}" fetchpriority="high">
  <div class="hero-txt">
    <h1><span>{E(t['name_first'])}</span><b>{E(t['name_last'])}</b></h1>
    <p class="roles">{E(t['roles'])}</p>
  </div>
</section>
<section class="reel wrap reveal" id="showreel">
  <p class="eyebrow">Showreel</p>
  <div class="player">
    <a class="poster" href="https://vimeo.com/1098971747/491d0dc05c" target="_blank" rel="noopener" aria-label="{'Αναπαραγωγή showreel' if lang=='el' else 'Play showreel'}"><img src="/img/tile-cinema.jpg" alt="" loading="lazy"><span class="play"></span></a>
  </div>
</section>
<script>
(function(){{var p=document.querySelector('#showreel .poster');if(!p)return;p.addEventListener('click',function(e){{e.preventDefault();var f=document.createElement('iframe');f.src='https://player.vimeo.com/video/1098971747?h=491d0dc05c&autoplay=1&title=0&byline=0&portrait=0';f.allow='autoplay; fullscreen; picture-in-picture';f.allowFullscreen=true;f.title='Diamantis Karanastasis showreel';p.parentNode.replaceChild(f,p);}});}})();
</script>
<section class="words wrap">
  <figure class="reveal"><img src="/img/words.jpg" alt="" loading="lazy"></figure>
  <div class="reveal">
    <p class="eyebrow">{E(t['words_h'])}</p>
    <p class="lede">{E(t['words'])}</p>
    <a class="more" href="/{t['paths']['bio']}">→ {E(t['words_more'])}</a>
  </div>
</section>
<section class="career">
  <div class="wrap"><p class="eyebrow">{E(t['career_h'])}</p></div>
  <div class="tiles">{tiles}</div>
</section>
<section class="quote wrap reveal">
  <blockquote>«Don’t count the days.<br>Make the days count.»<cite>Muhammad Ali</cite></blockquote>
</section>
<section class="moments">
  <div class="wrap"><p class="eyebrow">{E(t['photos_h'])}</p></div>
  <div class="slider">
    <button class="nav prev" aria-label="{'Προηγούμενη' if lang=='el' else 'Previous'}">&#8592;</button>
    <div class="strip" tabindex="0">{moments}</div>
    <button class="nav next" aria-label="{'Επόμενη' if lang=='el' else 'Next'}">&#8594;</button>
  </div>
  <div class="lb" role="dialog" aria-modal="true" hidden>
    <button class="lb-x" aria-label="{'Κλείσιμο' if lang=='el' else 'Close'}">&times;</button>
    <button class="lb-p" aria-label="{'Προηγούμενη' if lang=='el' else 'Previous'}">&#8592;</button>
    <img alt="">
    <button class="lb-n" aria-label="{'Επόμενη' if lang=='el' else 'Next'}">&#8594;</button>
    <span class="lb-c"></span>
  </div>
  <div class="wrap"><a class="more" href="https://www.instagram.com/diamond_karanastasis/" target="_blank" rel="noopener">→ Instagram @diamond_karanastasis</a></div>
</section>"""

def inner(lang, key):
    d = PAGES[lang][key]
    body = d["body"]
    if "GALLERY_THEATRE" in body:
        g = "".join(f'<figure class="reveal"><img src="/img/{i}.jpg" alt="{E(c)}" loading="lazy"><figcaption>{E(c)}</figcaption></figure>' for i, c in GALLERY_THEATRE[lang])
        body = body.replace("GALLERY_THEATRE", f'<div class="gallery">{g}</div>')
    return f"""
<section class="phead">
  <img src="/img/{d['img']}.jpg" alt="" fetchpriority="high">
  <div class="phead-txt wrap"><h1>{E(d['title'])}</h1></div>
</section>
<section class="epi wrap reveal"><blockquote>{E(d['q'])}<cite>{E(d['qa'])}</cite></blockquote></section>
<article class="prose wrap">{body}</article>"""

def contact(lang):
    t = L[lang]; d = CONTACT[lang]
    return f"""
<section class="phead">
  <img src="/img/{d['img']}.jpg" alt="" fetchpriority="high">
  <div class="phead-txt wrap"><h1>{E(d['title'])}</h1></div>
</section>
<section class="contact wrap">
  <p class="eyebrow">{E(d['h'])}</p>
  <p class="lede">{E(t['contact_p'])}</p>
  <a class="bigmail" href="mailto:{MAIL}">{MAIL}</a>
</section>"""

def write(path, s):
    full = os.path.join(OUT, path, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(s)

for lang in ("el", "en"):
    t = L[lang]
    write(t["paths"]["home"], shell(lang, "home", "", home(lang)))
    for key in ("bio", "theatre", "tv", "cinema"):
        write(t["paths"][key], shell(lang, key, PAGES[lang][key]["title"], inner(lang, key)))
    write(t["paths"]["contact"], shell(lang, "contact", CONTACT[lang]["title"], contact(lang)))

# 404
open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(
    shell("el", "home", "404", '<section class="contact wrap" style="padding-top:20vh"><p class="eyebrow">404</p><p class="lede">Η σελίδα δεν βρέθηκε. / Page not found.</p><a class="more" href="/">→ Αρχική / Home</a></section>'))
print("built")
