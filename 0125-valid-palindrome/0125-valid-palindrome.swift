class Solution {
    func isPalindrome(_ s: String) -> Bool {
        
        let cleanedString = s.replacingOccurrences(of: "[^a-zA-Z0-9]", with: "", options: .regularExpression).lowercased()
        let reversedString = String(cleanedString.reversed())
        return cleanedString == reversedString
     
    
        
    }
}