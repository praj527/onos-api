// Copyright 2020-present Open Networking Foundation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package config

import "github.com/google/uuid"

// ID is an identifier type
type ID string

// Index is the index of an object
type Index uint64

// Revision is a revision number
type Revision uint64

// NewUUID generates a new uuid
func NewUUID() uuid.UUID {
	newUUID, err := uuid.NewUUID()
	if err != nil {
		newUUID = uuid.New()
	}
	return newUUID
}
