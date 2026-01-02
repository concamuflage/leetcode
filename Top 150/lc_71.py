class Solution:
    def simplifyPath(self, path: str) -> str:

        # the key is to split by "/"
        string_array = path.split("/")
        result = []
        index = 0
        while index < len(string_array):
            # we should check from the first element
            # so that ".." can correctly pop the previous element that appeared in it.
            # I initially started appending from the last, which is wrong.
            
            sub_string = string_array[index]
            if sub_string == "..":
                if result:
                    result.pop()
            elif sub_string != "." and sub_string != "" :
                result.append(sub_string)
            index += 1
        result_string = ""
        result.reverse()
        while result:
            result_string += "/" + result.pop()
        if not result_string:
            result_string = "/"
        return result_string


sol = Solution()
print(sol.simplifyPath("//")) #/
print(sol.simplifyPath("/home/")) #/home
print(sol.simplifyPath("/home//foo/")) # /home/foo/
print(sol.simplifyPath("/home/user/Documents/../Pictures")) #/home/user/Pictures
print(sol.simplifyPath("/../")) #/
print(sol.simplifyPath("/.../a/../b/c/../d/./")) # "/.../b/d"
print(sol.simplifyPath("/.../a/../b/c/../d/./.")) # "/.../b/d"
print(sol.simplifyPath("/a/./b/../../c/")) #/c