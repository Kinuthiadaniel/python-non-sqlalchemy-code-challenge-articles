class Article:

    all_articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and (5<= len(value) <= 50):
            self._title = value
        else:
            return "Title characters must be 5 to 50 characters"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return "Author must be of instance author"
        
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
            

class Author:
    def __init__(self, name):
       self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (len(value) > 0):
            self._name = value
        else:
            return "Author name must have more than 0 characters"    
                


    def articles(self):
        return [article for article in Article.all_articles if article.author == self ]

        

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self,magazine, title)

    def topic_areas(self):
        pass

class Magazine:
   
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        
        

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            return "Category must be getter than 0 characters"
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value,str) and 2<=len(value)<=16:
            self._name = value
            
        else:
            return "Name must be greater then 2 and 16 characters"


    def articles(self):
        return self._articles

    def contributors(self):
        author = [article.author for article in self._articles]
        return list(set(author))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

ag =Magazine("rsc","xsscs")
ag2 = Magazine("new","ols")
ag.name = "hello"
print(ag.name)
ag2.name = 6
print(ag2.name)

