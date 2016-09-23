import fresh_tomatoes # fresh_tomatoes which contains server side programe
import media # contains the Movie class

# instances of Movie class
hackers = media.Movie("Hackers",
               """Dade, banned from using a computer until 18, grows up to be an even bigger 
                  hacker than his childhood pranks. Along with his friends, he discovers the
                  plot of an evil genius to unleash a lethal virus.
               """,
               "http://goo.gl/TNc9wm",
               "https://youtu.be/Rn2cf_wJ4f4?t=15")
    
pirates_of_silicon_valley = media.Movie("Pirates of Silicon Valley",
               """The accomplishments of visionaries Steve Jobs (Noah Wyle) and Bill Gates 
                  (Anthony Michael Hall) evolutionize the 20th century.
               """,
               "http://goo.gl/x0Saa0",
               "https://youtu.be/lEyrivrjAuU?t=2")
social_network = media.Movie("The Social Network",
               """Mark Zuckerberg creates a social networking site,
                  Facebook, with the help of his friend Eduardo Saverin. But soon,
                  a string of lies tears their relationship apart even as Facebook connects people.
               """,
               "http://goo.gl/cPkEXQ",
               "https://youtu.be/lB95KLmpLR4?t=8")
her = media.Movie("Her",
               """A soulful man earns a living by writing personal letters for other people.
                  Left heartbroken after his marriage ends, Theodore becomes fascinated with
                  a new operating system which reportedly develops into an intuitive and unique 
                  entity in its own right. He starts the program and meets Samantha, whose bright 
                  voice reveals a sensitive, playful personality. Though friends initially, the
                  relationship soon deepens into love.
               """,
               "http://goo.gl/kCrQTh",
               "https://youtu.be/ne6p6MfLBxc")
Gladiator = media.Movie("Gladiator",
               """Commodus takes over power and demotes Maximus, one of the preferred generals of his
                  father and predecessor, Emperor Marcus Aurelius. Maximus is relegated to fighting
                  till death as a gladiator.
               """,
               "http://goo.gl/R001HF",
               "https://youtu.be/lTmlYKiLBHI")
Troy = media.Movie("Troy",
               """A prince falls for a king's wife and takes her along with him to Troy.
                  The king's brother then uses this as an excuse to rage war on Troy
                  and realise his own selfish motives.
               """,
               "http://goo.gl/elisFA",
               "https://youtu.be/VzsfyxACV7M")

# appending movies in a list
movies = [hackers,pirates_of_silicon_valley,social_network,her,Gladiator,Troy]
# calling the function from fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
