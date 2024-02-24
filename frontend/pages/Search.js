import { StatusBar } from 'expo-status-bar';
import {SafeAreaView, StyleSheet, Text, View, TextInput, Image, ScrollView, Pressable} from 'react-native';
import {React, useState} from 'react'; 
import Ionicon from 'react-native-vector-icons/Ionicons';
import Filter from './Filter';

export default function App({navigation}) {
    const [search, setSearch] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const placeNames = ['Koala Craft']
    const placeAddresses = ['601 W Rosemary St.']
    const placeCities = ['Chapel Hill']
    const placeStates = ['NC']
    const placeZips = ['27516']
    const placeDistances = [0.3]
    const placeDescription = ['Arts & Crafts']
    const placeTags = ['Women-owned']

  return (
    <ScrollView>
    <View style={styles.container}>
    <SafeAreaView style={styles.search}>
        <TextInput
        style={styles.searchBar}
        placeholder="Search"
        onChangeText={setSearch}
        value={search}
        />
        {/* make pressable that takes you to Filter.js */}
        <Pressable
            onPress={() => navigation.navigate('Filter')}
        >
            <Ionicon name="filter-circle" size={30} color="#F2C5BE" />
        </Pressable>
    </SafeAreaView>
        <View style={styles.place}>
        <View style={styles.placeContainer}>
            <View style={styles.left}>
                <Text style={styles.header1}>
                    {placeNames[0]}
                </Text>
                <View style={styles.description}><Text style={styles.descripText}>{placeDescription[0]}</Text></View>
                <Text>{placeAddresses[0]}</Text>
                <Text>{placeCities[0]}, {placeStates[0]} {placeZips[0]}</Text>
                <Text style={styles.italic}>{placeDistances[0]} miles away</Text>
            </View>
            <Image
                source={require('../assets/Koala Craft.jpeg')}
                style={{ width: 124, height: 115 }}
            />
        </View>
        <View style={styles.bottom}>
            <View style={styles.tags}><Text style={styles.tagText}>{placeTags[0]}</Text></View>
            <Ionicon name="heart-outline" size={30} color="#F2C5BE" />
        </View>
        </View>
      <StatusBar style="auto" />
    </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
    header1: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    italic: {
        fontStyle: 'italic',
        color: '#A9A9A9',
    },
  container: {
    flex: 1,
    backgroundColor: '#F5F7FB',
    alignItems: 'center',
    justifyContent: 'center',
  },
  searchBar: {
    height: 40,
    width: 300,
    margin: 12,
    padding: 10,
    borderWidth: 1,
    borderColor: '#C4AAA6',
    borderRadius: 20,
  },
  placeContainer: {
    flexDirection: 'row',
  },
    left: {
        flex: 1,
    },
    tags: {
        backgroundColor: '#F2C5BE',
        borderRadius: 10,
        padding: 7,
        margin: 5,
        alignSelf: 'flex-start'
    },
    tagText: {
        color: '#FFFF',
        fontSize: 11,
    },
    place: {
        backgroundColor: '#F5F7FB',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'white',
        borderRadius: 10,
        margin: 20,
        padding: 10,
    },
    bottom: {
        marginTop: 10,
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    descripText: {
        fontSize: 12,
    },
    description: {
        backgroundColor: '#F5F7FB',
        borderRadius: 10,
        padding: 7,
        margin: 5,
        alignSelf: 'flex-start'
    },
    search: {
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
    },
});
