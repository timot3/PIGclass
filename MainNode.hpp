//
// Created by Justin Wang on 10/18/2019.
//

#ifndef PIGCLASS_MAINNODE_HPP
#define PIGCLASS_MAINNODE_HPP

#include <vector>
#include <string>

//#include "DisjointSet.cpp"

class MainNode {
private:
    std::vector<MainNode*> parents;
    std::vector<MainNode*> children;
    std::string id;
//    std::string course_name;
//    DisjointSet *prereqOrs;
public:
    int hashId;

    MainNode(std::string id);

    //Getters
    const std::vector<MainNode*> &getParents() const;

    const std::vector<MainNode*> &getChildren() const;

    const std::string &getId() const;

    const std::string &getCourseName() const;

    void addParent(MainNode &node);

    void addChild(MainNode &node);
};


#endif //PIGCLASS_MAINNODE_HPP
