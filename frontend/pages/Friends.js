import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, Pressable, Button, TextInput} from 'react-native';
import Modal from "react-native-modal";
import React, { useState } from 'react';


export default function App() {
    const [membersVisible, setMembersVisible] = useState(false);
    const [addMemberVisible, setAddMemberVisible] = useState(false);
    const [addGroupVisible, setAddGroupVisible] = useState(false);
    const [groupName, setGroupName] = useState('');
    const [members, setMembers] = useState([]);

    const addGroup = () => {
        // add the new group to the list of groups
        groups.push({name: groupName});
        // close the modal
        setAddGroupVisible(false);
    }

    const friends = 
    [
        {
            name: 'Sol Hacks',
            bio: 'I love sunflower seeds!'
        },
        {
            name: 'Giraffe George',
            bio: 'Favorite sport: running'
        },
        {
            name: 'Penguin Pedro',
            bio: 'Art is my passion'
        },
        {
            name: 'Lion Leo',
            bio: 'Love horiscopes'
        },
        {
            name: 'Tiger Tony',
            bio: 'Top chef'
        }
    ]

    const groups =
    [
        {
            name: 'Girls Who Code',
        },
        {
            name: 'Travelers',
        },
        {
            name: 'Foodies',
        }

    ]

  return (
    <View style={styles.container}>
      <View style={styles.section}>
        <Text style={styles.header1}>Friends</Text>
        <ScrollView horizontal={true}>
            {/* for each friend in friends, render a View component */}
            {friends.map((friend) => {
                return (
                    <View style={styles.friend}>
                        <Text style={styles.friendName}>{friend.name}</Text>
                        <Text style={styles.friendBio}>{friend.bio}</Text>
                    </View>
                );
            })}
        </ScrollView>
      </View>
      <View style={styles.section}> 
        <View style={styles.buttonGroup}>
            <Text style={styles.header1}>Groups</Text>
            <Pressable style={styles.addGroup} onPress={() => (setAddGroupVisible(true))}>
                <Text style={styles.plus}>+</Text>
            </Pressable>
            <Modal isVisible={addGroupVisible}>
                <View style={styles.addGroupForm}>
                    <Text style={styles.friendBio}>New Group Name</Text>
                    <TextInput style={styles.formInput} placeholder="New Group Name" onChangeText={(text) => setGroupName(text)} />
                    <Pressable style={styles.addButton} onPress= {addGroup}>
                        <Text style={styles.submitMember}>Add Group</Text>
                    </Pressable>

                </View>
                <Button title="Close" onPress={() => setAddGroupVisible(false)} />
            </Modal>

        </View>
        <ScrollView>
            {/* for each group in groups, render a View component */}
            {groups.map((group) => {
                return (
                    <View style={styles.friend}>
                        <Text style={styles.friendName}>{group.name}</Text>
                        <View style={styles.buttonGroup}>
                            <Pressable style={styles.viewMember} onPress={() => (setMembersVisible(true)) }>
                                <Text style={styles.buttonName}> View Members </Text>
                                <Modal isVisible={membersVisible}>
                                    <View style={styles.friend}>
                                        {friends.map((friend) => {
                                            return (
                                                <Text style={styles.friendName}>{friend.name}</Text>
                                            );
                                        })}
                                    </View>
                                    <Button title="Close" onPress={() => setMembersVisible(false)} />
                                </Modal>
                            </Pressable>
                            <Pressable style={styles.addMember} onPress={() => (setAddMemberVisible(true))}>
                                <Text style={styles.buttonName}> Add Member </Text>
                                <Modal isVisible={addMemberVisible}>
                                    <View style={styles.addMemberForm}>
                                        <Text style={styles.friendBio}>Add by username</Text>
                                        <TextInput style={styles.formInput} placeholder="Member Username" onChangeText={(text) => setMembers([...members, text])} />
                                        <Pressable style={styles.addButton} onPress={() => alert('pressed add member')}>
                                            <Text style={styles.submitMember}>Add Member</Text>
                                        </Pressable>
                                    </View>
                                    <Button title="Close" onPress={() => setAddMemberVisible(false)} />
                                </Modal>
                            </Pressable>
                        </View>
                    </View>
                );
            })}
        </ScrollView>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F7FB',
    paddingTop: 50,
  },
  section: {
    padding: 20,
    margin: 10,
  },
  header1: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  friend: {
    backgroundColor: '#ffff',
    padding: 10,
    margin: 10,
    borderRadius: 10,
  },
  friendName: {
    fontSize: 16,
    fontWeight: 'bold',
  },
    friendBio: {
        fontStyle: 'italic',
    },
    addGroup: {
        padding: 10,
        borderRadius: 10,
        shadowColor: 'gray',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 2 },
        margin: 10,
        width: 40,
        backgroundColor: 'pink',
    },
    viewMember: {
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        height: 40,
        shadowColor: 'gray',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 2 },
    },
    addMember: {
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        height: 40,
        shadowColor: 'gray',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 2 },
    },
    plus: {
        color: 'white',
        fontSize: 16,
        textAlign: 'center',
    },
    buttonGroup: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    formInput: {
        height: 40,
        borderColor: 'pink',
        borderWidth: 1,
        padding: 10,
        margin: 10,
        borderRadius: 10,
    },
    addButton: {
        backgroundColor: 'pink',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        height: 40,
        shadowColor: 'gray',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 2 },
    },
    submitMember: {
        color: '#FFFF',
        fontSize: 16,
        textAlign: 'center',
    },
    addMemberForm: {
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        alignItems: 'center',
    },
    buttonName: {
        fontSize: 16,
        textAlign: 'center',
        color: 'pink',
    },
    addGroupForm: {
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
        margin: 10,
        alignItems: 'center',
    },

});
