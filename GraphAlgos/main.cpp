#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <unordered_set>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <queue>

#include "MainNode.hpp"

std::unordered_map<std::string, int> hash_table;

void buildMainGraph(std::vector<MainNode*> &graph, std::vector<std::string> csvFiles);

void getSubgraph(std::unordered_set<MainNode *> &v, MainNode &node);

int main() {

    std::vector<std::string> csvFiles = {"C:\\Users\\Justin Wang\\CLionProjects\\PIGclass\\data\\cs_courses.csv", "C:\\Users\\Justin Wang\\CLionProjects\\PIGclass\\data\\ece_courses.csv"};
    std::vector<MainNode*> graph;
    buildMainGraph(graph, csvFiles);


    std::cout << "Build Finished" << std::endl;

    std::cout << "Tree with " + std::to_string(graph.size()) + " nodes" << std::endl;

    std::string target_test_class = "CS 446";

    std::unordered_set<MainNode *> prereqs;
    getSubgraph(prereqs, *graph[hash_table[target_test_class]]);

    std::cout << "The prereq graph of " + target_test_class + " is: " << std::endl;
    for (std::unordered_set<MainNode *>::iterator it = prereqs.begin(); it != prereqs.end(); it++) {
        std::cout << (*it)->getId() + ", ";
    }
    std::cout << std::endl;
}

void buildMainGraph(std::vector<MainNode*> &graph, std::vector<std::string> csvFiles) {

    int counter = 0;

    for (std::string file_name : csvFiles) {
        std::ifstream in_file(file_name);
        std::string line;
        while (std::getline(in_file, line)) {
            //Split by ',' character
            std::stringstream string_stream(line);
            std::string segment;
            std::vector<std::string> split_string;
            while (std::getline(string_stream, segment, ',')) {
                split_string.push_back(segment);
            }
            std::string course_id = split_string[0];
            //If key is not in table add it to the table
            if (hash_table.find(course_id) == hash_table.end()) {
                hash_table[course_id] = counter;
                counter++;

                MainNode *cur_node = new MainNode(course_id);
                graph.push_back(cur_node);
            }

            MainNode *cur_node = graph[hash_table[course_id]];

            for (int i = 1; i < split_string.size(); i+=2) {
                std::string related_course_id = split_string[i];
                int flag = stoi(split_string[i + 1]);

                //Check that the flag is an integer
                std::string check = std::to_string(flag);
                if (check != split_string[i + 1]) {
                    throw 1;
                }

                //For now only care about all courses with flag <= 1
                if (flag <= 1) {

                    if (hash_table.find(related_course_id) == hash_table.end()) {
                        hash_table[related_course_id] = counter;
                        counter++;
                        MainNode *related_node = new MainNode(related_course_id);
                        graph.push_back(related_node);
                    }

                    MainNode *related_node = graph[hash_table[related_course_id]];

                    //Add the connections to one another
                    cur_node->addParent(*related_node);
                    related_node->addChild(*cur_node);

                }
            }
        }
    }
}

void getSubgraph(std::unordered_set<MainNode*> &v, MainNode &node) {
    std::queue<MainNode *> queue;

    v.insert(&node);
    queue.push(&node);
    while (!queue.empty()) {
        MainNode *cur = queue.front();
        queue.pop();
        for (MainNode *p : cur->getParents()) {
            if (v.find(p) == v.end()) {
                v.insert(p);
                queue.push(p);
            }
        }
    }
}

//std::vector<MainNode> BuildMainTree()