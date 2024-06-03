// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBa62dPvlAEL840kz8kIbRrBy-O23pkOzs",
  authDomain: "ctfhelp-geminiapi.firebaseapp.com",
  projectId: "ctfhelp-geminiapi",
  storageBucket: "ctfhelp-geminiapi.appspot.com",
  messagingSenderId: "794510601571",
  appId: "1:794510601571:web:06bfe20f8fca1673ec3756",
  measurementId: "G-RV5RB8BFZX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);