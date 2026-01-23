import random
import string

source = [
    'This is a sentence.',
    'A word is a basic element of language that carries meaning, can be used on its own, and is uninterruptible.',
    'Despite the fact that language speakers often have an intuitive grasp of what a word is, there is no consensus among linguists on its definition and numerous attempts to find specific criteria of the concept remain controversial.',
    'Different standards have been proposed, depending on the theoretical background and descriptive context; these do not converge on a single definition.',
    'Some specific definitions of the term "word" are employed to convey its different meanings at different levels of description, for example based on phonological, grammatical or orthographic basis.',
    'oh  what is a word anyway, other than a sequence of letters with spaces on either side, and nothing interesting, like bananas or platypuses',
    'Philosophy is a systematic study of general and fundamental questions concerning topics like existence, reason, knowledge, value, beauty, mind, and language.',
    'It is a rational and critical inquiry that reflects on its methods and assumptions.',
    'Historically, many of the individual sciences, such as physics and psychology, formed part of philosophy.',
    'However, they are considered separate academic disciplines in the modern sense of the term.',
    'Influential traditions in the history of philosophy include Western, ArabicPersian, Indian, and Chinese philosophy.',
    'Western philosophy originated in Ancient Greece and covers a wide area of philosophical subfields.',
    'A central topic in ArabicPersian philosophy is the relation between reason and revelation.',
    'Indian philosophy combines the spiritual problem of how to reach enlightenment with the exploration of the nature of reality and the ways of arriving at knowledge.',
    'Chinese philosophy focuses principally on practical issues about right social conduct, government, and self-cultivation.',
    'Never let your sense of morals prevent you from doing what is right.',
    'The unexamined life is not worth living',
    'He who thinks great thoughts, often makes great errors',
    'Even while they teach, men learn',
    'We are what we repeatedly do. Excellence, then, is not an act, but a habit',
    'Life must be understood backward',
    'But it must be lived forward',
    'You can discover more about a person in an hour of play than in a year of conversation',
    'It is one thing to show a man that he is in error, and another to put him in possession of truth',
    'The only thing I know is that I know nothing',
    'The secret of happiness, you see is not found in seeking more, but in developing the capacity to enjoy less.',
    'When it is obvious that goals can\'t be reached, don\'t adjust the goals, but adjust the action steps.',
    'It is what you read when you don\'t have to that determines what you will be when you can\'t help it',
    'No amount of anxiety makes any difference to anything that is going to happen',
    'Prejudices are what fools use for reason',
    'Happiness depends upon ourselves',
    'We do not describe the world we see.',
    'We see the world we can describe',
    'What did you do as a child that made the hours pass like minutes',
    'Herein lies the key to your earthly pursuits',
    'What labels me, negates me.',
    'It is not true that people stop pursuing dreams because they grow old, they grow old because they stop pursuing dreams',
    'The menu is not the meal',
    'Out of suffering have emerged the strongest souls; the most massive characters are seared with scars',
]

def generate_word_level():
    """Generate sentence using word-level Markov chain"""
    data = []
    starters = []

    # Split the source into sentences
    sentences = [s for i in source for s in i.split('. ')]

    for i in sentences:
        translator = str.maketrans('', '', string.punctuation + '0123456789')
        x = i.translate(translator)
        words = x.split()
        if words:
            starters.append(words[0])
        for v in words:
            data.append(v)
        data.append('.')

    # Generate sentence
    sentence = [random.choice(starters)]
    while sentence[-1] != '.' and len(sentence) < 50:  # Prevent infinite loops
        poss = []
        for idx, a in enumerate(data[:-1]):
            if a == sentence[-1]:
                poss.append(data[idx + 1])
        if poss:
            sentence.append(random.choice(poss))
        else:
            sentence.append('.')

    # Build output
    out = ''
    for i in sentence:
        if i != '.':
            out += ' ' + i
        else:
            out += i
    return out.strip()

def generate_char_level(length=100):
    """Generate text using character-level Markov chain"""
    # Combine all source text
    text = ' '.join(source)
    # Remove extra punctuation but keep sentence structure
    translator = str.maketrans('', '', '0123456789')
    text = text.translate(translator)

    # Build character transitions
    transitions = {}
    for i in range(len(text) - 1):
        char = text[i]
        next_char = text[i + 1]
        if char not in transitions:
            transitions[char] = []
        transitions[char].append(next_char)

    # Start with a capital letter if possible
    starters = [c for c in text if c.isupper()]
    if not starters:
        starters = [text[0]]

    current = random.choice(starters)
    result = current

    for _ in range(length - 1):
        if current in transitions and transitions[current]:
            next_char = random.choice(transitions[current])
            result += next_char
            current = next_char
        else:
            break

    # Try to end at a reasonable punctuation
    if not result.endswith(('.', '!', '?')):
        result += '.'

    return result

def generate_ngram(n=2, max_words=20):
    """Generate sentence using N-gram Markov chain"""
    data = []
    starters = []

    # Split the source into sentences
    sentences = [s for i in source for s in i.split('. ')]

    for i in sentences:
        translator = str.maketrans('', '', string.punctuation + '0123456789')
        x = i.translate(translator)
        words = x.split()
        if words:
            starters.append(tuple(words[:n-1]) if n > 1 else words[0])
        for v in words:
            data.append(v)
        data.append('.')

    # Build n-gram transitions
    transitions = {}
    for i in range(len(data) - n):
        key = tuple(data[i:i+n-1]) if n > 1 else data[i]
        next_word = data[i+n-1]
        if key not in transitions:
            transitions[key] = []
        transitions[key].append(next_word)

    # Generate sentence
    if n == 1:
        current = random.choice(starters)
        sentence = [current]
    else:
        current = random.choice(starters)
        sentence = list(current)

    while len(sentence) < max_words:
        if current in transitions and transitions[current]:
            next_word = random.choice(transitions[current])
            sentence.append(next_word)
            if next_word == '.':
                break
            if n > 1:
                current = tuple(sentence[- (n-1):])
            else:
                current = next_word
        else:
            sentence.append('.')
            break

    # Build output
    out = ' '.join(sentence)
    return out

def main():
    print("=== Random Sentence Generator ===")
    print("Available modes:")
    print("1. word - Word-level Markov chain (most coherent)")
    print("2. char - Character-level Markov chain (most creative)")
    print("3. ngram - N-gram Markov chain (configurable coherence)")

    while True:
        try:
            mode_choice = input("\nChoose mode (1-3) or 'q' to quit: ").strip().lower()
            if mode_choice == 'q':
                print("Goodbye!")
                return
            elif mode_choice == '1' or mode_choice == 'word':
                mode = 'word'
                break
            elif mode_choice == '2' or mode_choice == 'char':
                mode = 'char'
                break
            elif mode_choice == '3' or mode_choice == 'ngram':
                mode = 'ngram'
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 'q'")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return

    # Get additional parameters based on mode
    if mode == 'char':
        while True:
            try:
                length = int(input("Enter maximum character length (default 100): ") or 100)
                if length > 0:
                    break
                else:
                    print("Length must be positive")
            except ValueError:
                print("Please enter a valid number")
    elif mode == 'ngram':
        while True:
            try:
                ngram_size = int(input("Enter n-gram size (2-5, default 2): ") or 2)
                if 2 <= ngram_size <= 5:
                    break
                else:
                    print("N-gram size must be between 2 and 5")
            except ValueError:
                print("Please enter a valid number")

    # Generate and display result
    print(f"\nGenerating with {mode} mode...")
    if mode == 'word':
        result = generate_word_level()
    elif mode == 'char':
        result = generate_char_level(length)
    elif mode == 'ngram':
        result = generate_ngram(ngram_size)

    print(f"\nGenerated ({mode} mode): {result}")

    # Ask if user wants to generate another
    while True:
        again = input("\nGenerate another? (y/n): ").strip().lower()
        if again == 'y' or again == 'yes':
            main()  # Recursive call to restart
            return
        elif again == 'n' or again == 'no':
            print("Goodbye!")
            return
        else:
            print("Please enter 'y' or 'n'")

if __name__ == '__main__':
    main()
