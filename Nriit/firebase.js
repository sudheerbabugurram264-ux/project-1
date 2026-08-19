// Firebase SDK
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.1.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.1.0/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/12.1.0/firebase-auth.js";

// Firebase Configuration
const firebaseConfig = {
  apiKey: "AIzaSyBzckuoLSm0sZSA13DQDeNvGagb64PixNw",
  authDomain: "nriit-college-app.firebaseapp.com",
  projectId: "nriit-college-app",
  storageBucket: "nriit-college-app.firebasestorage.app",
  messagingSenderId: "1008750055748",
  appId: "1:1008750055748:web:8c939edc3bd79d242f4711",
  measurementId: "G-9G3LP0VB2L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

// Initialize Authentication
const auth = getAuth(app);

export { db, auth };