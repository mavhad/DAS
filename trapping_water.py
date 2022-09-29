def fill(height: list[int]):
    l,r = 0, len(height)-1
    lmax,rmax=height[l],height[r]
    res = 0
  
    while l<r: 
        if lmax<rmax:
            l+=1
            lmax = max(lmax,height[l])
            res += lmax - height[l]
        else:
            r-=1
            rmax = max(rmax,height[r])
            res += rmax-height[r]

    print(res)


fill(height = [8, 8, 2, 4, 5, 5, 1])







