//
//  runpython.swift
//  ntcia
//
//  Created by Adam Mason on 22/02/2024.
//

import Foundation
//
//  ContentView.swift
//  ntcia
//
//  Created by Adam Mason on 22/02/2024.
//

import SwiftUI
import PythonKit

func RunPython() -> PythonObject {
    let sys = Python.import("sys")
    sys.path.append("/Users/adamhenley/Documents/GitHub/SMS-Dev1")
    let file = Python.import("pythonscripthere")
    
    let running = file.get_result()
    print(running)
    return running
}

