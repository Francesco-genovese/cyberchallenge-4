def count_patterns(N, M, alph, s):
    if not s or not set(s).intersection(alph):
        return 0

    # Creiamo un dizionario per tenere traccia delle occorrenze di ogni carattere nell'alfabeto
    alpha_count = {}
    for c in alph:
        alpha_count[c] = 0

    # Contiamo le occorrenze di ogni carattere nella stringa S
    for c in s:
        alpha_count[c] += 1

    # Troviamo il minimo numero di ripetizioni necessarie per coprire ogni carattere di S
    min_repeats = min(alpha_count.values())

    # Se min_repeats è zero, restituiamo zero
    if min_repeats == 0:
        return 0

    # Calcoliamo il massimo numero di occorrenze di R necessarie
    max_repeats = min(M // min_repeats, len(s) // min_repeats)

    # Contiamo il numero di copie di R necessarie per coprire completamente la stringa S
    count = 0
    for i in range(1, max_repeats + 1):
        if i * min_repeats >= M:
            break
        if all(alpha_count[c] * i <= M for c in alph):
            count = i

    return count

if __name__ == "__main__":
    T = int(input().strip())

    for _ in range(T):
        N, M = map(int, input().strip().split())
        alph = input().strip()
        s = input().strip()
        result = count_patterns(N, M, alph, s)
        print(result)
