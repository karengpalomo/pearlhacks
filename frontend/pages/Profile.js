import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList, Pressable } from 'react-native';
import Ionicons from 'react-native-vector-icons/Ionicons';


export default function Profile() {
    const firstName = 'Sol';
    const lastName = 'Hacks';
    const age = 21;
    const occupation = 'Aviation';
    const location = 'Chapel Hill, NC';
    const bio = 'I love sunflower seeds!';
    const interests = ['travel', 'hiking', 'coding', 'music', 'food'];

  return (
    <View style={styles.page}>
        <Text style={styles.header1}>{firstName} {lastName}</Text>
        <View style={styles.container}>
            <Text style={styles.header2}>Personal Info</Text>
            <View style={styles.info}>
                <Text style={styles.p}>Age </Text>
                <Text style={styles.p}>{age}</Text>
            </View>
            <View style={styles.info}>
                <Text style={styles.p}>Occupation </Text>
                <Text style={styles.p}>{occupation}</Text>
            </View>
            <View style={styles.info}>
                <Text style={styles.p}>Location </Text>
                <Text style={styles.p}>{location}</Text>
            </View>
            <View style={styles.info}>
                <Text style={styles.p}>Bio </Text>
                <Text style={styles.p}>{bio}</Text>
            </View>
        </View>
        <View style={styles.container}>
            <Text style={styles.header2}>Interests</Text>
            <View style={styles.interests_container}>
                {/* // for each interest in interests, render a Text component */}
                {interests.map((interest) => {
                    return <View style={styles.tag}><Text style={styles.tagtext}>{interest}</Text></View>;
                })}
                <Pressable style={styles.addButton} onPress={() => alert('pressed add interest')}>
                    <Text style={styles.tagtext}> + </Text>
                </Pressable>
            </View>
        </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
    page: {
        flex: 1,
        backgroundColor: '#F5F7FB',
        alignItems: 'center',
        justifyContent: 'center',
      },
  container: {
    backgroundColor: '#fff',
    padding: 20,
    borderRadius: 10,
    margin: 10,
    width: '90%',
  },
    interests_container: {
        backgroundColor: '#fff',
        width: '90%',
        marginTop: 10,
        alignItems: 'center',
        flexDirection: 'row',
        flexWrap: 'wrap',
    },
    header1: {
        fontSize: 24,
        fontWeight: 'bold',
    },
    header2: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    p: {
        fontSize: 16,
    },
    tag: {
        backgroundColor: '#F2C5BE',
        borderRadius: 10,
        padding: 7,
        margin: 5,
    },
    tagtext: {
        color: '#FFFF',
        fontSize: 16,
    },
    info: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        margin: 10,
    },
    friendButton: {
        backgroundColor: '#F2C5BE',
        borderRadius: 5,
        padding: 10,
        margin: 10,
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        borderColor: '#C4AAA6',
        borderWidth: 0.5,
    },
    buttons: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    addButton: {
        backgroundColor: '#C4AAA6',
        borderRadius: 10,
        padding: 7,
        margin: 5,
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,

    },

});
