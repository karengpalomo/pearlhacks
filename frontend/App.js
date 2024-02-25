import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import SearchScreen from './pages/Search';
import ItinerariesScreen from './pages/Itineraries';
import FriendsScreen from './pages/Friends';
import ChatScreen from './pages/Chat';
import ProfileScreen from './pages/Profile';
import FilterScreen from './pages/Filter';
import Itineraries from './pages/Itineraries';
import AddItineraries from './components/AddItineraries';
import Ionicons from 'react-native-vector-icons/Ionicons';
import 'react-native-gesture-handler';
import { createStackNavigator } from '@react-navigation/stack';

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

function Root() {
  return (
    <Tab.Navigator
    initialRouteName='Search'
      screenOptions={({ route }) => ({
        headerShown: false,
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;
          if (route.name === 'Search') {
            iconName = focused
              ? 'search-circle'
              : 'search-circle-outline';
          } else if (route.name === 'Itineraries') {
            iconName = focused ? 'list-circle' : 'list-circle-outline';
          } else if (route.name === 'Friends') {
            iconName = focused ? 'people-circle' : 'people-circle-outline';
          } else if (route.name === 'Chat') {
            iconName = focused ? 'chatbubble-ellipses' : 'chatbubble-ellipses-outline';
          } else if (route.name === 'Profile') {
            iconName = focused ? 'person-circle' : 'person-circle-outline';
          }
          return <Ionicons name={iconName} size={size} color={color} />;
        },
        
        tabBarActiveTintColor: '#C4AAA6',
        tabBarInactiveTintColor: 'gray',
        tabBarStyle: {
          backgroundColor: 'white',
          borderTopWidth: 0,
        },
      })}
    >
      <Tab.Screen name="Search" component={SearchScreen}/>
      <Tab.Screen name="Itineraries" component={ItinerariesScreen} />
      <Tab.Screen name="Friends" component={FriendsScreen} />
      <Tab.Screen name="Chat" component={ChatScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
    <View style={styles.container}>
    <NavigationContainer independent={true}>
      <Stack.Navigator>
        <Stack.Screen options={{headerShown: false}} name="Back" component={Root}/>
        <Stack.Screen name="Filter" component={FilterScreen} />
      </Stack.Navigator>
    </NavigationContainer>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#19173D',
    justifyContent: 'center',
  },
  header1: {
    color: '#B0E9FF',
    fontSize: 30,
    marginLeft: 20,
  },
  header2: {
    color: '#B0E9FF',
    fontSize: 20,
    marginLeft: 20,
  },
  
});
