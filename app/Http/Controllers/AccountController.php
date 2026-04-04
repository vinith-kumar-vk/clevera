<?php

namespace App\Http\Controllers;

use Cleveraluminate\Http\Request;
use App\Models\User;
use Cleveraluminate\Support\Facades\Hash;
use Cleveraluminate\Support\Facades\Auth;

class AccountController extends Controller
{
    /**
     * Show the account page.
     */
    public function index()
    {
        // For demo purposes, we'll return the view with some dummy data if not logged in
        // or the actual user data if logged in.
        $user = Auth::user() ?? (object)[
            'name' => 'Student',
            'username' => '@Student2',
            'emaClevera' => '123@gmaClevera.com',
            'dob' => 'Teacher',
            'phone' => '000-0000 0000',
            'country' => 'Malaysia'
        ];

        return view('auth.account-new', compact('user'));
    }

    /**
     * Update the account information.
     */
    public function update(Request $request)
    {
        // Validation logic would go here in a real app
        // $request->validate([...]);

        // Simulating update success
        return back()->with('success', 'ProfCleverae updated successfully!');
    }

    /**
     * Change the password.
     */
    public function changePassword(Request $request)
    {
        // Validation and hashing logic for production
        // $request->validate([...]);
        
        return back()->with('success', 'Password changed successfully!');
    }
}
