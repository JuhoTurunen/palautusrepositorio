from matchers import And, Or, All, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, querry = All()):
        self.querry_object = querry

    def plays_in(self, team):
        return QueryBuilder(And(self.querry_object, PlaysIn(team)))

    def has_at_least(self, amount, target):
        return QueryBuilder(And(self.querry_object, HasAtLeast(amount, target)))

    def has_fewer_than(self, amount, target):
        return QueryBuilder(And(self.querry_object, HasFewerThan(amount, target)))
    
    def one_of(self, *queries):
        return QueryBuilder(Or(*queries))
    
    def build(self):
        return self.querry_object
