class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        cur_color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        def dfs(sr, sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == cur_color and image[sr][sc] != color:
                image[sr][sc] = color
                dfs(sr+1,sc) # Down
                dfs(sr-1,sc) # Up
                dfs(sr,sc+1) # Right
                dfs(sr,sc-1) # Left

        dfs(sr,sc)

        return image
        
    #     if image == None or image[sr][sc] == color:
    #         return image
        
    #     self.fill(image,sr,sc,image[sr][sc], color)
    #     return image

    # def fill(self,image,r,c,initial,color):
    #     if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initial:
    #         return
    #     image[r][c] = color
    #     self.fill(image, r+1, c, initial, color) # down
    #     self.fill(image, r-1, c, initial, color) # up
    #     self.fill(image, r, c+1, initial, color) # right
    #     self.fill(image, r, c-1, initial, color) # left
