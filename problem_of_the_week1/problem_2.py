def flood_fill(image, sr, sc, new_color):
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    def fill(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != original_color:
            return
        
        image[r][c] = new_color

        
        fill(r+1, c)  
        fill(r-1, c)  
        fill(r, c+1)  
        fill(r, c-1) 

    fill(sr, sc)
    return image


n, m = map(int, input().split())

image = []
for _ in range(n):
    row = input().split()
    image.append(row)

sr, sc = map(int, input().split())
C = input().strip()
result = flood_fill(image, sr, sc, C)
for row in result:
    print(" ".join(row))
