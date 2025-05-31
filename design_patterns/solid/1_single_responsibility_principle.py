#!/usr/bin/env python3

class Journal:
    """
     Journal class for showing Single Resposibility Principle.
     A module should be responsible to one, and only one, actor.
     A class should have only one reason to change.

     As an example, consider a module that compiles and prints a report. 
     Imagine such a module can be changed for two reasons. 
     First, the content of the report could change. 
     Second, the format of the report could change. 
     These two things change for different causes. 
     The single-responsibility principle says that these two aspects of the problem 
     are really two separate responsibilities, and should, therefore, 
     be in separate classes or modules. It would be a bad design to couple two things that 
     change for different reasons at different times.
    """

    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self) -> str:
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     with open(filename, 'w+') as fh:
    #         fh.write(str(self))
    #         fh.close()
    

class PersistentManager:
    def save_to_file(journal, filename):
        with open(filename, 'w+') as fh:
            fh.write(str(journal))
            fh.close()

if __name__ == "__main__":
    j = Journal()
    j.add_entry("I went to office today.")
    j.add_entry("I went to market yesterday.")
    print(f'Journal entries:\n{j}')

    file = r'd:\temp\journal.txt'
    PersistentManager.save_to_file(j, file)
