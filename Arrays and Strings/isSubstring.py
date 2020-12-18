
class isSubstring:
      def is_rotation(self,s1, s2):
        if len(s1)!=len(s2):
          return False
        return self.is_substring(s1+s1,s2)

      def is_substring(self,s1,s2):
        if len(s2) > len(s1):
          return False


        for i in range(len(s1)-len(s2)+1):
          is_a_substring = True

          for j in range(len(s2)):
            if s1[i+j]!=s2[j]:
              is_a_substring = False
              break
          if is_a_substring:
            return True

        return False 







if __name__ == '__main__':
  obj  = isSubstring()
  s1 = 'tabletop'
  s2 = 'optablet'
  print(f"The answer to s1 being a substring to s2 is : {obj.is_rotation(s1,s2)}")