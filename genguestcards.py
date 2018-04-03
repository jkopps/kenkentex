import sys
import csv

playCommands = dict(zip(
(
    'Hamlet',
    'Much Ado About Nothing',
    'Twelfth Night',
    'Romeo and Juliet',
    'Taming of the Shrew',
    "Midsummer Night's Dream",
    'As You Like It',
    'Antony and Cleopatra'
),
(
    '\\setPuzzleHamlet',
    '\\setPuzzleMuchAdo',
    '\\setPuzzleTwelfthNight',
    '\\setPuzzleRomeoAndJuliet',
    '\\setPuzzleTamingOfTheShrew',
    '\\setPuzzleMidsummerNights',
    '\\setPuzzleAsYouLikeIt',
    '\\setPuzzleAntonyAndCleopatra'
)
))

if __name__ == '__main__':
    TableAssignments = []
    with open('assignments.csv', 'r') as fh:
        rdr = csv.reader(fh)
        for row in rdr:
            guests, table = row
            assert table in playCommands, 'Unrecognized play: "%s"' % table
            TableAssignments.append((guests, table))

    sys.stdout.write("""
\\input{playPuzzles}

\\begin{document}
""")

    for (guests, play) in TableAssignments:
        sys.stdout.write('%s\n' % playCommands[play])
        sys.stdout.write('\\makePuzzleCard{%s}\n\n' % guests)

    sys.stdout.write('\\end{document}\n')

    with open('numcards.tex', 'w') as fh:
        fh.write('\\def\\numcards{%d}\n' % len(TableAssignments))
