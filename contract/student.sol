// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract StudentGradeManagement {
    struct Student {
        uint256 id;
        string name;

    }

    struct Score {
        string subject;
        uint score;
        string appraise;
    }

    mapping(uint => Student) public students;
    mapping(uint => Score[]) public scores; 
    mapping(address => bool) public handlers; 
    uint256 public studentCount;
    address public admin;

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier onlyHandlers() {
        require(handlers[msg.sender], "Only handler can perform this action");
        _;
    }

    // 设置权限
    function setHandler(address _handler) public onlyAdmin{
        handlers[_handler] = true;
    }

    // 添加学生
    function addStudent(uint256 _id, string memory _name) public onlyHandlers {
        Student memory s;
        s.id = _id;
        s.name = _name;
        studentCount++;
        students[_id]=s;
    }

    // 删除学生
    function deleteStudent(uint256 _studentId) public onlyHandlers {
        delete students[_studentId];
        studentCount--;
    }

    // 添加学生成绩
    function addScore(uint _id,string memory _subject,uint _score) public  onlyHandlers{

        scores[_id].push(Score({
            subject:_subject,
            score:_score,
            appraise:  ( _score >=60 && _score <80) ? "B" : ( _score > 80) ? "A" : ( _score<60) ? "D" : "C" 
        }));
    }

    // 修改学生成绩
    function updateScore(uint _id,uint _num,uint _score) public  onlyHandlers{
        scores[_id][_num].score = _score;
    }

    // 修改学生姓名
    function modifyStudentName(uint256 _studentId, string memory _newName) public  onlyHandlers {
        students[_studentId].name = _newName;
    }

    // 获取学生信息
    function getStudentInfo(uint256 _studentId) public view onlyHandlers returns (Student memory) {
        return students[_studentId];
    }

    // 获取学生成绩
    function getStudentScore(uint256 _studentId) public view onlyHandlers returns (Score[] memory) {
        return scores[_studentId];
    }

    // 设置管理员
    function setAdmin(address _address) public  {
        admin = _address;
    }
}
