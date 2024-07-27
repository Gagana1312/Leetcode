class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {

        let rows = matrix.count
        let cols = matrix[0].count

        var row = rows-1
        var col = 0

        while row>=0 && col < cols{
            let number = matrix[row][col]

            if number == target {
                return true
            }

            if number > target {
                row-=1
            }
            if number < target{
                col+=1
            }
        }
        return false
        
    }
}