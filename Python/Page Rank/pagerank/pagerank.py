import os
import random
import re
import sys
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
   """
    model= dict()
    outgoing_links= corpus[page]
    count_outgoing_links= len(outgoing_links)
    #if a page is chosen at random from the corpus
    p1 = (1-damping_factor)/len(corpus)
    #if a page is chosen from the given page
    if count_outgoing_links!=0:
        p2= (damping_factor)/(count_outgoing_links) 
    else: # a page having no links is interpreted as one having link to every page inc itself
        p2= (damping_factor)/len(corpus)

    for page in corpus:
        if count_outgoing_links==0:
            model[page]= p1+ p2
        elif page in outgoing_links:
            model[page] = p1 + p2
        else:
            model[page] = p1

    return model        





def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.
     """
    samples=[]
    count_pages = len(corpus) 
    allpages= []
    for page in corpus:
        allpages.append(page)
    #pick a random starting page from the corpus
    current_page= random.choice(allpages)
    samples.append(str(current_page))
    #repeat for n samples
    for i in range(n):
         #get the transition model for the chosen page
             model = transition_model(corpus,current_page,damping_factor)
             #draw an element from the transtition model(pseudorandomly) according to the probability distribution
             pages_choice= [page for page in model]
             pages_distribution = [prob for prob in model.values()]
             current_page= random.choice(random.choices(pages_choice,weights= pages_distribution, k=1))
             samples.append(str(current_page))
    #no of occurences of each page
    occurences= Counter(samples)
    Page_Rank = dict()
    for page in corpus:
        Page_Rank[page]= occurences[page]/n
    
    return Page_Rank

    

    

    


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.
    """
    Page_Rank= dict()
    n= len(corpus)
    #change in page rank value after each iteration
    change = dict()
    #initilze the dicionary with 1/n for each page
    for page in corpus:
        Page_Rank[page]= (1/n)
        change[page]= 0

    #iteratively calculate pagerank untill convergence
    while True:
        for page in corpus:
            #if page is chosen randomly from corpus
            p1= ((1-damping_factor)/n)
            #if page is chosen from current page
            p2= 0
            for link in corpus:
                if link == page:  #ignore current page
                    continue
                else:
                    if page in corpus[link]:
                        p2= p2 + Page_Rank[link]/len(corpus[link])
                        #page having no links is interpreted as one having one link to every page inc itself
                    elif len(corpus[link])==0:
                        p2= p2 + Page_Rank[link]/n
                         
            p2= p2* damping_factor
            #update change in page rank
            change[page] = (p1+ p2) - Page_Rank[page]
            #update page's pagerank
            Page_Rank[page]= p1 + p2
        #check for convergence
        counter= 0
        for page in change:
            if change[page]<(0.001):
                counter= counter +1
        if counter==n:
            break
    
    return Page_Rank
            


        


if __name__ == "__main__":
    main()
