P = int(input("Enter your favourite number: "))

n = int(input("Enter number of songs: "))

playlist = [0] * n
duplicate = 0
total_duration = 0
invalid = False

for i in range(n):
    playlist[i] = int(input("Enter song duration: "))
    if playlist[i] <= 0:
        print("Invalid Playlist")
        invalid = True
        break
    total_duration += playlist[i]

if not invalid:
    for i in range(n):
        for j in range(i + 1, n):
            if playlist[i] == playlist[j]:
                duplicate += 1

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", n)

    if total_duration < 300:
        print("Category: Too Short Playlist")
        print("Recommendation: Add more songs")

    elif total_duration > 3600:
        print("Category: Too Long Playlist")
        print("Recommendation: Reduce playlist length")

    elif duplicate > 0:
        print("Category: Repetitive Playlist")
        print("Recommendation: Add variety")

    elif total_duration >= 300 and total_duration <= 3600:
        print("Category: Balanced Playlist")
        print("Recommendation: Good listening session")

    else:
        print("Category: Irregular Playlist")
        print("Recommendation: Adjust song durations")
