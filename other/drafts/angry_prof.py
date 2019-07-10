"""
Merit: Usage of filter function
"""

def is_on_time(arrival):
    return arrival <= 0

def angry_prof(k, a):
    if len(list(filter(is_on_time, a))) < k:
        return "YES"
    return "NO"

if __name__ == "__main__":
    a = [97, -55, 48, -22, 99, -46, 40, 11, 5, -61, 78, -20, 44, 22, -8, 82, 24, -62, 0, 52, -79, 68, -73, -81, 33, 60, -99, -99, 59, -13, 90, -26, 84, 90, 76, 36, -45, 79, 87, 48, 59, -36, 42, -6, -13, 21, -19, -21, 39, -40]
    print(angry_prof(20, a))
    a = [-50, 58, 24, 69, 81, 84, 72, 50, -85, 99, 42, 13, 90, 90, -81, -36, 55, 4, -69, -76, 55, 42, -84, -5, -67, 13, -54, 59, 2, 6, 21, 68, 89, 8, 98, 8, -48, -33, -48, 54, -46, 29, 46, 97, -90, -33, -97, -92, 25, 96]
    print(angry_prof(18, a))
    a = [-36, 14, -60, 28, -50, 56, 94, -99, -39, 28, 0, -47, 59, -35, 39, 15, -4, -49, 85, -43, -77, 38, -49, -67, 92, -43, 29, 82, 41, -26, 61, 60, -23, -81, -90, -96, -77, 90, 24, -14, 5, 12, 0, 26, 16, 78, -46, 47, 51, 31]
    print(angry_prof(26, a))
